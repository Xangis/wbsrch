# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.language import IdentifyLanguage
import codecs

class Command(BaseCommand):
    help = """Performs semi-manual or automatic language categorization for domains.

    To perform automatic categorization, which kind of works but is very experimental, you should use a command something like this:

        time python manage.py categorize_language -c -t -a an,ca,cs,cy,de,el,es,et,eu,fi,fr,gl,hr,hu,it,lt,lv,nl,pl,pt,ro,sl,sv,sw,tr,rw,xh,zu -q -o -j -i 12000000 -m 200000 | grep -v UnicodeDecodeError

    To perform automatic language blocking, which kind of works but is very experimental, you should use a command something like this:

        python manage.py categorize_language -c -t -b am,ar,as,az,be,bg,bn,cn,dz,fa,gu,he,hi,hy,id,ja,jv,ka,kk,km,kn,ko,ku,ky,lo,mk,ml,mn,mr,ms,ne,or,pa,ps,ru,si,sq,sr,ta,te,th,tl,ug,uk,ur,vi,zh -q -i 10000000 | grep -v UnicodeDecodeError

    To perform automatic language blocking for only domains ending in .ua:

        python manage.py categorize_language -c -t -b am,ar,as,az,be,bg,bn,cn,dz,fa,gu,he,hi,hy,id,ja,jv,ka,kk,km,kn,ko,ku,ky,lo,mk,ml,mr,mn,mr,ms,ne,or,pa,ps,ru,si,sq,sr,ta,te,th,tl,ug,uk,ur,vi,zh -q -i 10000000 -u .ua | grep -v UnicodeDecodeError

    To automatically tag sites as english, which kind of works but is very experimental, you should use a command something like this (note the use of -n so we only tag with higher-confidence data):

        python manage.py categorize_language -e -o -t -q -n 3 -i 2000 | grep -v UnicodeDecodeError
"""

    option_list = BaseCommand.option_list + (
        make_option('-m', '--maxurls', default=100000, action='store', type='int', dest='maxurls', help='Max number of URLs in domain to start with, in descending order. (default=100000)'),
        make_option('-i', '--items', default=100, action='store', type='int', dest='items', help='Number of items to process (default=100)'),
        make_option('-n', '--numpageminimum', default=1, action='store', type='int', dest='numpageminimum', help='Minimum number of pages required to process a domain (default=1).'),
        make_option('-o', '--onlyautotag', default=False, action='store_true', dest='onlyautotag', help='Only auto-tag, nothing else. Requires -e or -a switch.'),
        make_option('-j', '--justnotenglish', default=False, action='store_true', dest='justnotenglish', help='Only prompt for items that detect as mostly (<10%) non-English (default=False)'),
        make_option('-e', '--autotagenglish', default=False, action='store_true', dest='autotagenglish', help='Auto-tag sites that detect as english (>95%). Supersedes skipping english in -j. (default=False)'),
        make_option('-c', '--confidentprompt', default=False, action='store_true', dest='confident', help='Only prompt for sites where confidence level in one language is over 90%. Works with -j (default=False)'),
        make_option('-a', '--autotag', default=None, action='store', type='string', dest='autotag', help='Automatically tag this comma-seperated list of language codes, only works with -c.'),
        make_option('-b', '--autoblock', default=None, action='store', type='string', dest='autoblock', help='Automatically block this comma-seperated list of language codes, only works with -c.'),
        make_option('-u', '--urlsuffix', default=None, action='store', type='string', dest='urlsuffix', help='Only check URLs with this suffix.'),
        make_option('-z', '--afterz', default=False, action='store_true', dest='afterz', help='Only check URLs with pages having a title after z. Can be combined with -0'),
        make_option('-0', '--beforezero', default=False, action='store_true', dest='beforezero', help='Only check URLs with pages having a title before zero. Can be combined with -z'),
        make_option('-p', '--urlprefix', default=None, action='store', type='string', dest='urlprefix', help='Only check URLs with this prefix.'),
        make_option('-r', '--rank', default=False, action='store_true', dest='rank', help='Check untagged domains in order of popularity rank.'),
        make_option('-q', '--quiet', default=False, action='store_true', dest='quiet', help='Quiet mode - do not log individual pages and titles to the console.'),
        make_option('-t', '--textminimum', default=False, action='store_true', dest='textminimum', help='Require at least 100 characters of text to count page for categorization.'),
        make_option('-d', '--domain', default=None, action='store', type='string', dest='domain', help='Only check this domain.'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load domain list from specified file. Ignores all options and categorizes/blocks everything.'),
    )

    def handle(self, *args, **options):
        maxurls = options.get('maxurls', 100000)
        maxitems = options.get('items', 50000)
        justnotenglish = options.get('justnotenglish', False)
        autotagenglish = options.get('autotagenglish', False)
        onlyautotag = options.get('onlyautotag', False)
        autotag = options.get('autotag', None)
        autoblock = options.get('autoblock', None)
        justdomain = options.get('domain', None)
        textminimum = options.get('textminimum', False)
        afterz = options.get('afterz', False)
        beforezero = options.get('beforezero', False)
        quiet = options.get('quiet', False)
        verbosity = int(options['verbosity'])
        numpageminimum = int(options['numpageminimum'])
        tagged_count = 0
        processed = 0
        if autotag:
            autotag = autotag.split(',')
        if autoblock:
            autoblock = autoblock.split(',')
        confident = options.get('confident', False)
        onlysuffix = options['urlsuffix']
        onlyprefix = options.get('urlprefix', None)
        rank = options.get('rank', False)
        print 'Max Items to Process: {0}, Max Num URLs Starting Point: {1}, Min starting point: {2}'.format(maxitems, maxurls, numpageminimum)
        counts = []
        result = None
        cursor = connection.cursor()
        uncategorized_domains = []
        if options['file']:
            autotagenglish = True
            onlyautotag = False
            confident = True
            autotag = language_list
            autoblock = blocked_language_list
            filename = options['file']
            domains = []
            numloaded = 0
            print('Loading domains to check from file: {0}'.format(filename))
            f = open(filename, 'rb')
            reader = codecs.getreader('utf8')(f)
            for line in reader.readlines():
                line = line.strip()
                uncategorized_domains.append(line)
            print('{0} domains loaded from file {1}.'.format(numloaded, filename))
        # We start with the domains having the most pages and descend.
        elif afterz or beforezero:
            autotagenglish = True
            onlyautotag = False
            confident = True
            autotag = language_list
            autoblock = blocked_language_list
            if afterz:
                # Should give us SELECT DISTINCT rooturl FROM site_info WHERE pagetitle > 'z'
                domainpages = SiteInfo.objects.filter(pagetitle__gt='ZZZZZZZZZZ').values_list('rooturl', flat=True).distinct()
                print('{0} domains found with title after Z.'.format(len(domainpages)))
                for domainpage in domainpages:
                    try:
                        domaininfo = DomainInfo.objects.get(url=domainpage)
                        if domaininfo.language_association or domaininfo.uses_language_subdirs or domaininfo.uses_langid:
                            continue
                        else:
                            uncategorized_domains.append(domainpage)
                    except:
                        uncategorized_domains.append(domainpage)
            if beforezero:
                # Should give us SELECT DISTINCT rooturl FROM site_info WHERE pagetitle < '0'
                domainpages = SiteInfoBeforeZero.objects.filter(pagetitle__lt='0').values_list('rooturl', flat=True).distinct()
                print('{0} domains found with title after Z.'.format(len(domainpages)))
                for domainpage in domainpages:
                    try:
                        domaininfo = DomainInfo.objects.get(url=domainpage)
                        if domaininfo.language_association or domaininfo.uses_language_subdirs or domaininfo.uses_langid:
                            continue
                        else:
                            uncategorized_domains.append(domainpage)
                    except:
                        uncategorized_domains.append(domainpage)
                print('{0} domains found with uncategorized language.'.format(len(uncategorized_domains)))
        else:
            if justdomain:
                query = "SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl = '{0}' GROUP BY rooturl;".format(justdomain)
            elif onlysuffix:
                query = "SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl ILIKE '%{0}' GROUP BY rooturl HAVING count(*) <= {1} ORDER BY count_total DESC LIMIT {2};".format(onlysuffix, maxurls, maxitems)
            elif onlyprefix:
                query = "SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl ILIKE '{0}%' GROUP BY rooturl HAVING count(*) <= {1} ORDER BY count_total DESC LIMIT {2};".format(onlyprefix, maxurls, maxitems)
            elif rank:
                query = 'SELECT alexa_rank AS count_total, url AS rooturl FROM dir_domaininfo WHERE language_association IS null AND alexa_rank IS NOT null AND uses_language_subdirs = false AND uses_language_query_parameter = false ORDER BY alexa_rank LIMIT {0};'.format(maxurls, maxitems)
            elif numpageminimum:
                query = 'SELECT count(*) AS count_total, rooturl FROM site_info GROUP BY rooturl HAVING count(*) >= {0} ORDER BY count_total DESC,RANDOM() LIMIT {1};'.format(numpageminimum, maxitems)
            else:
                query = 'SELECT count(*) AS count_total, rooturl FROM site_info GROUP BY rooturl HAVING count(*) <= {0} ORDER BY count_total DESC,RANDOM() LIMIT {1};'.format(maxurls, maxitems)
            #cursor.execute('SELECT count(*), rooturl FROM site_info GROUP BY rooturl ORDER BY count(*) DESC LIMIT ' + str(maxitems))
            print('Running query: {0}'.format(query))
            cursor.execute(query)
            domain_counts = cursor.fetchall()
            for domain in domain_counts:
                processed += 1
                # Bail if we hit our page minimum -- we're done.
                if domain[0] < numpageminimum:
                    print('Domain {0} is below our minimum of {1}, done gathering.'.format(domain[1], domain[0]))
                    break
                # Skip domains above maximum number of pages.
                if domain[0] > maxurls:
                    continue
                try:
                    domaininfo = DomainInfo.objects.get(url=domain[1])
                    if domaininfo.language_association or domaininfo.uses_language_subdirs or domaininfo.uses_langid:
                        continue
                    else:
                        uncategorized_domains.append(domain[1])
                except:
                    uncategorized_domains.append(domain[1])
        for domain in uncategorized_domains:
            urls = SiteInfo.objects.filter(rooturl=domain)
            if rank and urls.count() < 1:
                print u'Domain {0} has no crawled pages.'.format(domain)
                try:
                    blocked = BlockedSite.objects.get(domain)
                    print 'Because it is marked as blocked for reason {0}'.foramt(blocked.reason)
                except:
                    pass
                continue
            total = 0
            english = 0
            scores = {}
            for url in urls:
                if textminimum and len(url.pagetext) < 100:
                    if verbosity >=2:
                        print 'Skipping page with less than 100 chars of text.'
                    continue
                total = total + 1
                idlang = IdentifyLanguage(url.pagetext)
                if idlang[0] == 'en':
                    english = english + idlang[1]
                if scores.has_key(idlang[0]):
                    scores[idlang[0]] = scores[idlang[0]] + idlang[1]
                else:
                    scores[idlang[0]] = idlang[1]
                title = url.pagetitle
                if not title:
                    title = url.pagefirsth2tag
                head = url.pagefirstheadtag
                if not head:
                    head = url.pagefirsth3tag
                if not quiet:
                    try:
                        print(u'{0} {1} [{2}] [{3}]'.format(
                            idlang, url.url, url.pagetitle, url.pagefirstheadtag))
                    except UnicodeEncodeError:
                        print('Page info is not valid unicode, cannot print')
            # If the URLs are blocked or removed between the time of querying domains and processing them,
            # as can happen running multi-day language processing, or running more than one, this prevents
            # divide by zero crashes.
            scores = sorted(scores.iteritems(), key=lambda item: item[1], reverse=True)
            print u'Scores for {0}: {1}'.format(domain, scores)
            if total:
                englishratio = (english * 100) / total
            else:
                englishratio = 0
                continue
            if autotagenglish and englishratio > 95:
                print u'Site {0} is mostly English - ratio {1} from {2} of {3}, auto-tagging as English'.format(domain, englishratio, english, total)
                input = 'en'
                tagged_count = tagged_count + 1
            elif autotagenglish and onlyautotag:
                print u'Not English. Skipping.'
                continue
            elif justnotenglish and englishratio > 45:
                if not quiet:
                    print u'Site is more than slightly English - {0} of {1}, skipping categorization.'.format(english, total)
                continue
            elif confident and (scores[0][1] < (0.86 * total)):
                if not quiet:
                    print u'Site is not at least 86% one language - {0}/{1} {2}, skipping categorization.'.format(scores[0][1], total, scores[0][0])
                continue
            else:
                # Prompt for what to do. If c
                if confident and autotag and (scores[0][0] in autotag):
                    print u'Auto-Tagging {0} as language {1} ({3}/{2} {1})]? '.format(domain, scores[0][0], total, scores[0][1])
                    input = scores[0][0]
                    tagged_count += 1
                elif confident and autoblock and (scores[0][0] in autoblock):
                    print u'Auto-Blocking {0} as unindexed language {1} ({3}/{2} {1})]? '.format(domain, scores[0][0], total, scores[0][1])
                    input = 'del'
                    tagged_count += 1
                elif autotag and onlyautotag:
                    if not quiet:
                        print u'Skipping {0} because we are in only-auto-tag mode and it could not be automatically tagged.'.format(domain)
                    input = 's'
                elif autoblock:
                    if not quiet:
                        print u'Skipping {0} because we are in auto-block mode and it could not be automatically blocked.'.format(domain)
                    input = 's'
                else:
                    input = raw_input(u'Tag {0} as: [q]uit/[s]kip/[i]nfix-tag/[u]rlparam-tag/[del]ete/[xx] lang ({1}/{2} En, {3}/{2} {4})]? '.format(total, english, total, scores[0][1], scores[0][0]))
                input = input.lower()
            if input == 'q':
                exit()
            elif input == 's':
                continue
            elif input == 'i':
                try:
                    dom = DomainInfo.objects.get(url=domain)
                except:
                    dom = DomainInfo()
                    dom.url = domain
                dom.uses_language_subdirs = True
                dom.save()
                continue
            elif input == 'u':
                try:
                    dom = DomainInfo.objects.get(url=domain)
                except:
                    dom = DomainInfo()
                    dom.url = domain
                dom.uses_language_query_parameter = True
                dom.save()
                continue
            elif input == 'del':
                try:
                    existing = BlockedSite.objects.get(url=domain)
                    # If the domain is already blocked, the URL must have been added erroneously.
                    # in that case, just delete it.
                    RemoveURLsForDomain(item.rooturl)
                except ObjectDoesNotExist:
                    langtoblock = scores[0][0]
                    site = BlockedSite()
                    site.url = domain
                    # TODO: Set reason to match language categorized as.
                    if langtoblock == 'ar' or langtoblock == 'fa':
                        # (20, 'Unindexed Language - Arabic or Farsi'),
                        site.reason = 20
                    elif langtoblock == 'am':
                        # (45, 'Unindexed Language - Amharic'),
                        site.reason = 45
                    elif langtoblock == 'as':
                        # (50, 'Unindexed Language - Assamese'),
                        site.reason = 50
                    elif langtoblock == 'az':
                        # (34, 'Unindexed Language - Azerbaijani'),
                        site.reason = 34
                    elif langtoblock == 'be':
                        # (59, 'Unindexed Language - Belarusian'),
                        site.reason = 59
                    elif langtoblock == 'bn':
                        # (60, 'Unindexed Language - Bengladeshi'),
                        site.reason = 60
                    elif langtoblock == 'dz':
                        # (56, 'Unindexed Language - Dzongkha'),
                        site.reason = 56
                    elif langtoblock == 'gu':
                        # (46, 'Unindexed Language - Gujarati'),
                        site.reason = 46
                    elif langtoblock == 'he':
                        # (22, 'Unindexed Language - Hebrew'),
                        site.reason = 22
                    elif langtoblock == 'hi':
                        # (23, 'Unindexed Language - Hindi'),
                        site.reason = 23
                    elif langtoblock == 'hy':
                        # (32, 'Unindexed Language - Armenian'),
                        site.reason = 32
                    elif langtoblock == 'id' or langtoblock == 'ms':
                        # (24, 'Unindexed Language - Indonesian or Similar'),
                        site.reason = 24
                    elif langtoblock == 'jv':
                        # (49, 'Unindexed Language - Javanese'),
                        site.reason = 49
                    elif langtoblock == 'ka':
                        # (31, 'Unindexed Language - Georgian'),
                        site.reason = 31
                    elif langtoblock == 'kk':
                        # (43, 'Unindexed Language - Kazakh'),
                        site.reason = 43
                    elif langtoblock == 'kn':
                        # (58, 'Unindexed Language - Kannada'),
                        site.reason = 58
                    elif langtoblock == 'ku':
                        # (47, 'Unindexed Language - Kurdish'),
                        site.reason = 47
                    elif langtoblock == 'ky':
                        # (44, 'Unindexed Language - Kyrgyz'),
                        site.reason = 44
                    elif langtoblock == 'ja':
                        # (25, 'Unindexed Language - Japanese'),
                        site.reason = 25
                    elif langtoblock == 'km':
                        # (26, 'Unindexed Language - Khmer'),
                        site.reason = 26
                    elif langtoblock == 'ko':
                        # (27, 'Unindexed Language - Korean'),
                        site.reason = 27
                    elif langtoblock == 'lo':
                        # (54, 'Unindexed Language - Lao'),
                        site.reason = 54
                    elif langtoblock == 'mk':
                        # (41, 'Unindexed Language - Macedonian'),
                        site.reason = 41
                    elif langtoblock == 'mn':
                        # (48, 'Unindexed Language - Mongolian'),
                        site.reason = 48
                    elif langtoblock == 'mr':
                        # (55, 'Unindexed Language - Marathi'),
                        site.reason = 55
                    elif langtoblock == 'ml':
                        # (60, 'Unindexed Language - Malayalam'),
                        site.reason = 60
                    elif langtoblock == 'ne':
                        # (52, 'Unindexed Language - Nepali'),
                        site.reason = 52
                    elif langtoblock == 'or':
                        # (57, 'Unindexed Language - Oriya'),
                        site.reason = 57
                    elif langtoblock == 'pa':
                        # (39, 'Unindexed Language - Punjabi'),
                        site.reason = 39
                    elif langtoblock == 'ps':
                        # (40, 'Unindexed Language - Pashto'),
                        site.reason = 40
                    elif langtoblock == 'ru' or langtoblock =='uk' or langtoblock == 'bg':
                        # (28, 'Unindexed Language - Russian or Other Cyrillic'),
                        site.reason = 28
                    elif langtoblock == 'si':
                        # (36, 'Unindexed Language - Sinhala'),
                        site.reason = 36
                    elif langtoblock == 'sq':
                        # (37, 'Unindexed Language - Albanian'),
                        site.reason = 37
                    elif langtoblock == 'sr':
                        # (33, 'Unindexed Language - Serbian'),
                        site.reason = 33
                    elif langtoblock == 'ta':
                        # (51, 'Unindexed Language - Tamil'),
                        site.reason = 51
                    elif langtoblock == 'te':
                        # (42, 'Unindexed Language - Telugu'),
                        site.reason = 42
                    elif langtoblock == 'th':
                        # (30, 'Unindexed Language - Thai'),
                        site.reason = 30
                    elif langtoblock == 'tl':
                        # (38, 'Unindexed Language - Tagalog'),
                        site.reason = 38
                    elif langtoblock == 'ug':
                        # (53, 'Unindexed Language - Uighur'),
                        site.reason = 53
                    elif langtoblock == 'ur':
                        # (35, 'Unindexed Language - Urdu'),
                        site.reason = 35
                    elif langtoblock == 'vi':
                        # (29, 'Unindexed Language - Vietnamese'),
                        site.reason = 29
                    elif langtoblock == 'zh':
                        # (21, 'Unindexed Language - Chinese'),
                        site.reason = 21
                    #elif langtoblock == 'or':
                    #    # TDOO: Add a reason for and 'or'
                    #    site.reason = 8
                    else:
                        # (8, 'Unindexed Language - Unspecified'),
                        site.reason = 8
                        print('Do not have a specific language block reason for language: {0}'.format(langtoblock))
                        break
                    site.save()
                    try:
                        dom = DomainInfo.objects.get(url=domain)
                    except:
                        dom = DomainInfo()
                        dom.url = domain
                    dom.language_association = langtoblock
                    dom.save()
                continue
                RequeueRankedKeywordsForDomain(domain)
                print 'Site {0} language blocked and all URLs deleted.'.format(domain)
            else:
                if input in language_list or input in ['fo', 'fy', 'oc', 'om', 'nap', 'eo']:
                    model = GetSiteInfoModelFromLanguage(input)
                    if model:
                        try:
                            dom = DomainInfo.objects.get(url=domain)
                        except:
                            dom = DomainInfo()
                            dom.url = domain
                        dom.language_association = input
                        dom.save()
                        if input != 'en':
                            urls = SiteInfo.objects.filter(rooturl=domain)
                            for url in urls:
                                print u'Moving ' + unicode(url) + u' to ' + input
                                MoveSiteTo(url, input)
                else:
                    print '{0} is not a valid language. Skipping'.format(input)
                    continue
        print('Finished. Processed {0} domains and {1} were not tagged. Number of auto-tagged items: {2}'.format(
          processed, len(uncategorized_domains), tagged_count))
