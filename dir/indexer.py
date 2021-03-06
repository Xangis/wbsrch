# -*- coding: utf-8 -*-

# This file implements the batch processing part of the indexer. It is meant to be run from a manage.py command.
# To see available options, run 'python manage.py index -h'
#
# This replaces the standalone index.py file that we were using until February 2014.
#
# To index a single term, call BuildIndexForTerm.

import time
from django.db import connection
from django.utils import timezone
from dir.models import *
from dir.utils import *
import datetime
import codecs
import math
from unidecode import unidecode


def Indexer(options):
    print(options)
    if options['justthisterm']:
        pendingindexes = [options['justthisterm']]
    elif options['pending']:
        pendingindexes = GetPendingIndexes(options['maxindexes'], options['offset'], options['language'], options['verbose'], options['random'])
    elif options['reindex']:
        pendingindexes = GetReindexes(options['maxindexes'], options['offset'], options['language'], options['verbose'], options['random'], options['quickness'], options['days'])
    elif options['file']:
        pendingindexes = LoadKeywordsFromFile(options['file'])
    else:
        print("You didn't give me anything to do. Anyhow, I'm done doing it.")
        return
    type = options.get('type', None)
    Index(pendingindexes, options['maxindexes'], options['sleep'], options['language'], options['verbose'], options['abbreviated'], type)


def RemoveFromPending(keywords, language=None):
    try:
        index_model = GetPendingIndexModelFromLanguage(language)
        existing = index_model.objects.get(keywords=keywords)
        existing.delete()
        return True
    except Exception:
        return False


def Index(pendingindexes, max, sleep=2, language=None, verbose=False, abbreviated=False, type=None):
    processedkeywords = 0
    removedfrompending = 0
    saved = 0
    notsaved = 0
    for keywords in pendingindexes:
        if verbose:
            print('Indexing: {0}'.format(keywords))
        was_saved = BuildIndexForTerm(keywords, language, verbose, abbreviated, type)
        if was_saved:
            saved = saved + 1
        else:
            notsaved = notsaved + 1
        if RemoveFromPending(keywords, language):
            removedfrompending = removedfrompending + 1
        processedkeywords = processedkeywords + 1
        if processedkeywords >= max:
            break
        time.sleep(sleep)
    print('Indexed {0} terms. {1} were saved and {2} were not saved. {3} terms were removed from the pending term database.'.format(
        processedkeywords, saved, notsaved, removedfrompending))


def LoadKeywordsFromFile(filename):
    pendingindexes = []
    numloaded = 0
    print('Loading pending indexes from file: {0}'.format(filename))
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader.readlines():
        pendingindexes.append(line)
        numloaded = numloaded + 1
    print('{0} Keywords loaded from {1}.'.format(numloaded, filename))
    return pendingindexes


def GetPendingIndexes(max, offset=0, language='en', verbose=False, random=False):
    pendingindexes = []
    index_model = GetPendingIndexModelFromLanguage(language)
    if random:
        pending = index_model.objects.all().order_by('?')[offset:max + offset]
    else:
        pending = index_model.objects.all().order_by('priority', 'date_added')[offset:max + offset]
    print('Loading pending indexes from {0} database: '.format(language))
    for item in pending:
        pendingindexes.append(item.keywords)
        if verbose:
            print(item.keywords)
    print('Loaded {0} pending indexes from database.'.format(len(pendingindexes)))
    return pendingindexes


def GetReindexes(max, offset=0, language='en', verbose=False, random=False, quickness=None, days=None):
    pendingindexes = []
    index_model = GetIndexModelFromLanguage(language)
    if days and days > 0:
        newest = (timezone.now() - datetime.timedelta(days=days))
        if verbose:
            print('Getting indexes before {0}, which is {1} days before now.'.format(newest, days))
        pending = index_model.objects.filter(date_indexed__lte=newest).order_by('date_indexed')[offset:max + offset]
    elif random:
        pending = index_model.objects.all().order_by('?')[offset:max + offset]
    else:
        pending = index_model.objects.all().order_by('date_indexed')[offset:max + offset]
    print('Loading stale indexes from {0} database: '.format(language))
    for item in pending:
        if quickness and quickness > 0:
            if item.index_time > quickness:
                if verbose:
                    print('Not adding "{0}" to queue because it took {1} seconds, longer than our limit of {2}'.format(
                        item.keywords, item.index_time, quickness))
                continue
        pendingindexes.append(item.keywords)
        if verbose:
            print(item.keywords)
    print('Loaded {0} stale indexes from database.'.format(len(pendingindexes)))
    return pendingindexes


def AddIndividualWords(ratings, keywords, type, lang='en'):
    """
    Gets data for the individual words of a multi-word phrase and merges them with the
    existing exact-phrase-match data, scoring each keyword's items according to the
    specified algorithm and adding them to the connection, combining scores where items
    show up more than once.

    Results are returned in sorted order, with highest value pages listed first.

    Available algorithms:
    full
    half
    loghalf
    cuberoot
    cuberootb
    fourthroot
    fourthrootb
    logdivide
    fourthrootandlog
    squareroot1200
    squareroot1100
    squareroot1050
    squareroot1025
    squareroot1000
    """
    print('We need to apply multiword algorithm {0} to our data.'.format(type))
    start = timezone.now()
    singlewords = keywords.split(' ')
    term_model = GetIndexModelFromLanguage(lang)
    for singleword in singlewords:
        #print u'Getting index for {0} to add to index for {1}.'.format(singleword, keywords)
        try:
            word = term_model.objects.get(keywords=singleword)
        except ObjectDoesNotExist:
            # Should we just skip words that aren't found, or should we index them too?
            # For now we're just skipping them. They'll theoretically eventually be indexed
            # if there are any results for them.
            try:
                print('Index term {0} not found, cannot use for calculations.'.format(singleword))
            except Exception:
                print('Index term (unprintable) not found, cannot use for calculations.')
            continue
        # No point in adding up a word with no results, and this way we don't have to worry about divide by zero.
        if not word.num_pages or word.num_pages == 0:
            print('Index term {0} has zero results, nothing to calculate.'.format(word.keywords))
            continue
        # All formula comments are spreadsheet formulas (assuming number of results for word in cell B2)
        # These formulas were calculated based on 8.8 million URLs in the English index and the index page
        # counts that resulted.
        #
        # As the index grows, we may need to adjust our factor calculations. Or we may not, since exact
        # phrase matches will become both more common and more heavily weighted and results will just
        # naturally improve as the index grows.
        if type == 'full':
            factor = 1.0
        elif type == 'half':
            factor = 0.5
        elif type == 'loghalf':
            # =1/POWER(2, (LOG(B2, 10)))
            factor = 1 / math.pow(2, (math.log(word.num_pages, 10)))
        elif type == 'cuberoot':
            # =100 - POWER(B2, 1/3)
            factor = 100.0 - math.pow(word.num_pages, (1.0 / 3.0)) / 100.0
        elif type == 'cuberootb':
            # =101 - POWER(B2, 1/3)
            factor = 101.0 - math.pow(word.num_pages, (1.0 / 3.0)) / 100.0
        elif type == 'fourthroot':
            # =(33.333 - POWER(B2, 1/4)) * 3
            factor = ((33.33 - math.pow(word.num_pages, (1.0 / 4.0))) * 3) / 100.0
        elif type == 'fourthrootb':
            # =(32.0 - POWER(B2, 1/4)) * 3
            factor = ((32.0 - math.pow(word.num_pages, (1.0 / 4.0))) * 3) / 100.0
        elif type == 'logdivide':
            # =1 / (LOG(B2, 10)+1)
            factor = 1.0 / (math.log(word.num_pages, 10) + 1.0)
        elif type == 'fourthrootandlog':
            # Takes the average of the fourthrootb and the logdivide calculations, but with slightly different
            # max/scaling factors.
            factora = ((29 - math.pow(word.num_pages, (1.0 / 4.0))) * 3) / 100.0
            factorb = 0.80 / (math.log(word.num_pages, 10) + 1.0)
            factor = (factora + factorb) / 2.0
        elif type == 'squareroot1200':
            # =(1200 - SQRT(B2)) / 1200
            factor = (1200.0 - math.sqrt(word.num_pages)) / 1200.0
        elif type == 'squareroot1100':
            # =(1100 - SQRT(B2)) / 1100
            factor = (1100.0 - math.sqrt(word.num_pages)) / 1100.0
        elif type == 'squareroot1050':
            # =(1050 - SQRT(B2)) / 1050
            factor = (1050.0 - math.sqrt(word.num_pages)) / 1050.0
        elif type == 'squareroot1025':
            # =(1025 - SQRT(B2)) / 1025
            factor = (1025.0 - math.sqrt(word.num_pages)) / 1025.0
        elif type == 'squareroot1000':
            # =(1000 - SQRT(B2)) / 1000
            factor = (1000.0 - math.sqrt(word.num_pages)) / 1000.0
        else:
            print('Invalid merge type algorithm {0}'.format(type))
            return ratings
        try:
            print('Merge factor for term {0} is {1} with {2} results'.format(singleword, factor, word.num_pages))
        except Exception:
            print('Merge factor for term (unprintable) is {0} with {1} results'.format(factor, word.num_pages))
        page_rankings = ujson.loads(word.page_rankings)
        for item in page_rankings:
            # print 'Checking {0} in page_rankings.'.format(item)
            points = item[1] * factor
            # print u'Item {0} is worth {1} points using factor {2}'.format(item, points, factor)
            found = False
            # TODO: Do this right.
            for i, existing in enumerate(ratings):
                if item[0] == existing[0]:
                    # print u'Adding {0} points to {1}'.format(points, ratings[i])
                    ratings[i][1] = existing[1] + points
                    found = True
                    break
            if not found:
                # print u'Adding [ {0} , {1} ]'.format(item[0], points)
                ratings.append([item[0], points])
    ratings.sort(key=lambda tup: tup[1], reverse=True)
    end_delta = timezone.now() - start
    print('Merging existing index terms took {0} seconds.'.format(end_delta.total_seconds()))
    return ratings


def BuildIndexForTerm(keywords, lang='en', verbose=False, abbreviated=False, type=None):
    """
    Builds an index of pages for a keyword or keyword phrase.
    """
    start = timezone.now()
    multiword = False
    if ' ' in keywords:
        multiword = True
    # We have to keep track of the number of previous queries and add from there because
    # when we index multiple terms, queries are additive.
    if verbose:
        prevqueries = len(connection.queries)
    keywords = keywords.strip()
    if len(keywords) < 1:
        if verbose:
            print('BuildIndexForTerm: Search term is empty. Refusing to index.')
        return False
    keywords = keywords.lower()
    term = None
    new = False
    term_model = GetIndexModelFromLanguage(lang)
    site_model = GetSiteInfoModelFromLanguage(lang)
    try:
        term = term_model.objects.get(keywords=keywords)
        if term.num_pages is None:
            term.num_pages = 0
    except ObjectDoesNotExist:
        term = term_model()
        term.keywords = keywords
        term.num_results = 0
        term.num_pages = 0
        new = True
    if verbose:
        print('{0} Indexing term ({1}): {2}'.format(timezone.now().isoformat(), lang, keywords))
        if term.num_results > 0:
            print('(Reindex) Term had {0} results and {1} pages last index on {2}'.format(term.num_results, term.num_pages, term.date_indexed))
    # We do not need lastcrawled, or firstcrawled. This may or may not save some effort.
    # However, leaving out pagetext saves a *lot* of effort and computation time.
    kp = '%' + keywords + '%' # Allow us to do raw ILIKE queries without formatting problems.
    spacelesskeywords = keywords.replace(' ', '%')
    asciikeywords = unidecode(spacelesskeywords)
    if spacelesskeywords != asciikeywords:
        print('Checking URL as {0}'.format(asciikeywords))
    akp = '%' + asciikeywords + '%'
    # Don't even bother selecting on page text, keywords, or description ILIKE for massive queries.
    # Since title, first head tag, and URL are most important. About 1.2% of queries fit this and
    # indexing them can be a multi-hour process on a slow server.
    #
    # On 2015-03-18 added a limit of 1 million rows to every query. Results for anything with a million rows will be crappy
    # and a popularity contest anyway, at least that gives us a chance of succeeding in our indexing.
    querystart = timezone.now()
    if term.num_pages > 100000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp])
    elif term.num_pages > 40000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp, kp])
    elif term.num_pages > 10000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp, kp, kp])
    # If we have more than 3000 results, ignore the specific page text because we can get what we
    # need from the head tag, url, keywords, description, and title (mostly).
    elif abbreviated or term.num_pages > 3000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, kp, kp, akp, kp, kp, kp])
    else:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR pagetext ILIKE " +
                     "%s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, kp, kp, kp, akp, kp, kp, kp])
    if verbose:
        print(sql_query.replace("%s", ("'" + kp + "'")))
    ratings = []
    if verbose:
        querydelta = timezone.now() - querystart
        print('Query took: {0} seconds'.format(querydelta.total_seconds()))
        print('{0} Calculating values.'.format(timezone.now().isoformat()))
    # Calculate the score for each page we've found.
    termcalcstart = timezone.now()
    for item in index_items:
        try:
            weight = CalculateTermValue(item, keywords, abbreviated, lang)
        # Any problem calculating the term's value and it gets a zero.
        except Exception:
            weight = 0
        ratings.append([item.id, weight])
    term.num_pages = len(ratings)
    # Sort by score
    if verbose:
        termcalcdelta = timezone.now() - termcalcstart
        print('Calculating term values took: {0} seconds'.format(termcalcdelta.total_seconds()))
        print('{0} Sorting index by score.'.format(timezone.now().isoformat()))
    ratings.sort(key=lambda tup: tup[1], reverse=True)
    ratings = ratings[0:5000]
    # Load existing terms for multi-word phrases.
    if multiword and type:
        ratings = AddIndividualWords(ratings, keywords, type, lang)
        # Re-trim the ratings so we're still at 5000 max.
        ratings = ratings[0:5000]
    term.keywords = keywords
    term.page_rankings = str(ratings)
    term.num_results = len(ratings)
    end_delta = timezone.now() - start
    term.index_time = end_delta.total_seconds()

    if verbose:
        print('{0} Saving index term.'.format(timezone.now().isoformat()))
    jsonify_start = timezone.now()
    # Don't save new index terms unless it has at least one result.
    saved = True
    if not new or term.num_pages > 0:
        if new and multiword:
            individualwords = term.keywords.split(' ')
            blocked = term_model.objects.filter(keywords__in=individualwords, actively_blocked=True).count()
            if blocked > 0:
                print('Marking this term as blocked because at least one of the words in it is blocked.')
                term.actively_blocked = True
        term.save()
        JsonifyIndexTerm(term, lang, verbose=verbose)
    else:
        if verbose:
            print('Not saving index term because it does not have at least one result.')
        saved = False
    jsonify_delta = timezone.now() - jsonify_start
    if verbose:
        print('{0} Done indexing: {1}, {2} results from {3} pages.'.format(timezone.now().isoformat(), keywords, term.num_results, term.num_pages))
        LogQueries(connection.queries[prevqueries:])
    try:
        print("Index Time for '{0}': {1} seconds, Jsonify Time: {2} seconds (includes ranking update), {3} pages, {4} results.".format(
            term.keywords, term.index_time, jsonify_delta.total_seconds(), term.num_pages, term.num_results))
    except Exception:
        pass
    return saved
