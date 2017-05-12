# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.language import NLTKLanguageDetect, IdentifyPageLanguage, IdentifyLanguage

class Command(BaseCommand):
    help = "Performs semi-manual language categorization for domains."

    option_list = BaseCommand.option_list + (
        make_option('-m', '--maxurls', default=100000, action='store', type='int', dest='maxurls', help='Max number of URLs in domain to start with, in descending order. (default=100000)'),
        make_option('-i', '--items', default=100, action='store', type='int', dest='items', help='Number of items to process (default=100)'),
        make_option('-o', '--onlyautotag', default=False, action='store_true', dest='onlyautotag', help='Only auto-tag, nothing else. Requires -e or -a switch.'),
        make_option('-j', '--justnotenglish', default=False, action='store_true', dest='justnotenglish', help='Only prompt for items that detect as mostly (<10%) non-English (default=False)'),
        make_option('-e', '--autotagenglish', default=False, action='store_true', dest='autotagenglish', help='Auto-tag sites that detect as english (>95%). Supersedes skipping english in -j. (default=False)'),
        make_option('-c', '--confidentprompt', default=False, action='store_true', dest='confident', help='Only prompt for sites where confidence level in one language is over 90%. Works with -j (default=False)'),
        make_option('-a', '--autotag', default=None, action='store', type='string', dest='autotag', help='Automatically tag this comma-seperated list of language codes, only works with -c.'),
        make_option('-b', '--autoblock', default=None, action='store', type='string', dest='autoblock', help='Automatically block this comma-seperated list of language codes, only works with -c.'),
        make_option('-u', '--urlsuffix', default=None, action='store', type='string', dest='urlsuffix', help='Only check URLs with this suffix.'),
        make_option('-p', '--urlprefix', default=None, action='store', type='string', dest='urlprefix', help='Only check URLs with this prefix.'),
        make_option('-r', '--rank', default=None, action='store', type='string', dest='rank', help='Check untagged domains in order of popularity rank.'),
        make_option('-d', '--domain', default=None, action='store', type='string', dest='domain', help='Only check this domain.'),
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
        if autotag:
            autotag = autotag.split(',')
        if autoblock:
            autoblock = autoblock.split(',')
        confident = options.get('confident', False)
        onlysuffix = options['urlsuffix']
        onlyprefix = options.get('urlprefix', None)
        rank = options.get('rank', False)
        print 'Max Items to Process: {0}, Max Num URLs Starting Point: {1}'.format(maxitems, maxurls)
        counts = []
        result = None
        cursor = connection.cursor()
        uncategorized_domains = []
        if justdomain:
            cursor.execute("SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl = '{0}' GROUP BY rooturl;".format(justdomain))
        elif onlysuffix:
            cursor.execute("SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl ILIKE '%{0}' GROUP BY rooturl HAVING count(*) < {1} ORDER BY count_total DESC LIMIT {2};".format(onlysuffix, maxurls, maxitems))
        elif onlyprefix:
            cursor.execute("SELECT count(*) AS count_total, rooturl FROM site_info WHERE rooturl ILIKE '{0}%' GROUP BY rooturl HAVING count(*) < {1} ORDER BY count_total DESC LIMIT {2};".format(onlyprefix, maxurls, maxitems))
        elif rank:
            cursor.execute('SELECT alexa_rank AS count_total, url AS rooturl FROM dir_domaininfo WHERE language_association IS null AND alexa_rank IS NOT null AND uses_language_subdirs = false AND uses_language_query_parameter = false ORDER BY alexa_rank LIMIT {0};'.format(maxurls, maxitems))
        else:
            cursor.execute('SELECT count(*) AS count_total, rooturl FROM site_info GROUP BY rooturl HAVING count(*) < {0} ORDER BY count_total DESC LIMIT {1};'.format(maxurls, maxitems))
        #cursor.execute('SELECT count(*), rooturl FROM site_info GROUP BY rooturl ORDER BY count(*) DESC LIMIT ' + str(maxitems))
        domain_counts = cursor.fetchall()
        for domain in domain_counts:
            try:
                domaininfo = DomainInfo.objects.get(url=domain[1])
                if domaininfo.language_association or domaininfo.uses_language_subdirs or domaininfo.uses_langid:
                    continue
            except:
                pass
            if domain[0] < maxurls:
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
                total = total + 1
                language = NLTKLanguageDetect(url.pagetext)
                pagelanguage = IdentifyPageLanguage(url.url, url.pagecontents)
                idlang = IdentifyLanguage(url.pagetext)
                if idlang[0] == 'en':
                    english = english + 1
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
                print u'{0} ({1}) {2} {3} [{4}] [{5}]'.format(
                    idlang, language, pagelanguage, url.url, url.pagetitle, url.pagefirstheadtag)
            # If the URLs are blocked or removed between the time of querying domains and processing them,
            # as can happen running multi-day language processing, or running more than one, this prevents
            # divide by zero crashes.
            scores = sorted(scores.iteritems(), key=lambda item: item[1], reverse=True)
            print u'Scores: {0}'.format(scores)
            if total:
                englishratio = (english * 100) / total
            else:
                continue
            if autotagenglish and englishratio > 95:
                print u'Site is mostly English - {0} of {1}, auto-tagging as English'.format(english, total)
                input = 'en'
            elif autotagenglish and onlyautotag:
                print u'Not English. Skipping.'
                continue
            elif justnotenglish and englishratio > 45:
                print u'Site is more than slightly English - {0} of {1}, skipping categorization.'.format(english, total)
                continue
            elif confident and (scores[0][1] < (0.86 * total)):
                print u'Site is not at least 86% one language - {0}/{1} {2}, skipping categorization.'.format(scores[0][1], total, scores[0][0])
                continue
            else:
                # Prompt for what to do. If c
                if confident and autotag and (scores[0][0] in autotag):
                    print u'Auto-Tagging {0} as language {1} ({3}/{2} {1})]? '.format(domain, scores[0][0], total, scores[0][1])
                    input = scores[0][0]
                elif confident and autoblock and (scores[0][0] in autoblock):
                    print u'Auto-Blocking {0} as unindexed language {1} ({3}/{2} {1})]? '.format(domain, scores[0][0], total, scores[0][1])
                    input = 'del'
                elif autotag and onlyautotag:
                    print u'Skipping {0} because we are in only-auto-tag mode and it could not be automatically tagged.'.format(domain)
                    input = 's'
                elif autoblock and onlyautotag:
                    print u'Skipping {0} because we are in only-auto-tag mode and it could not be automatically blocked.'.format(domain)
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
                    site = BlockedSite()
                    site.url = domain
                    site.reason = 8
                    site.save()
                RequeueRankedKeywordsForDomain(domain)
                print 'Site {0} language blocked and all URLs deleted.'.format(domain)
            else:
                if input in language_list or input in ['gl', 'eu', 'fo', 'fy', 'oc', 'om', 'nap', 'eo']:
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
