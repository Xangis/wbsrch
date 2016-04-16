
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, BlockedSite
from dir.utils import GetSiteInfoModelFromLanguage
import time
import codecs

class Command(BaseCommand):
    help = """
    Due to redirects and other things, domains don't always have a DomainInfo record when they have URLs
    in the database. This is used to fix that by creating DomainInfo records where they're missing.
    """
    option_list = BaseCommand.option_list + (
        #make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        #make_option('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.'),
        make_option('-b', '--blockedsite', default=False, action='store_true', dest='blockedsite', help='Used blocked site list to ensure domain info.'),
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for domains (default=en). It is dumb to use not english because if a domain is in another table, it has been categorized and has a domain info.'),
        make_option('-t', '--tagverify', default=False, action='store_true', dest='tagverify', help='Verify language tags for non-English domains found in language table (default=False)'),
        #make_option('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=15, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=15)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-i', '--info', default=False, action='store_true', dest='info', help='Just print the unknown domains (typically used with -f)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load domain list from specified file.'),
        # TODO: Make an option to fill in nulls vs update already-queried domains.
    )

    def handle(self, *args, **options):
        filename = options.get('file', None)
        info = options.get('info', False)
        if filename:
            f = open(filename, 'rb')
            reader = codecs.getreader('utf8')(f)
            for line in reader.readlines():
                line = line.strip().lower()
                # Do not queue anything less than 2 characters long.
                if len(line) < 2:
                    continue
                try:
                    di = DomainInfo.objects.get(url=line)
                except ObjectDoesNotExist:
                    if info:
                        print u'{0}'.format(line)
                    else:
                        di = DomainInfo()
                        di.url = line
                        print u'Added domain entry for {0}'.format(di.url)
                        di.save()
            exit()
        start = timezone.now()
        site_model = GetSiteInfoModelFromLanguage(options['language'])
        max = options['max']
        offset = options['offset']
        blockedsite = options['blockedsite']
        if blockedsite:
            domains = BlockedSite.objects.all().values('url').distinct().order_by('url')[offset:(offset+max)]
        else:
            domains = site_model.objects.all().values('rooturl').distinct().order_by('rooturl')[offset:(offset+max)]
        processed = 0
        added = 0
        langassoc = 0
        for domain in domains:
            if blockedsite:
                dom = domain['url']
            else:
                dom = domain['rooturl']
            if dom.startswith('http:') or dom.startswith('https:'):
                print u'{0} has an incorrect rooturl.'.format(dom)
                continue
            try:
                di = DomainInfo.objects.get(url=dom)
            except ObjectDoesNotExist:
                di = DomainInfo()
                if blockedsite:
                    di.url = domain['url']
                else:
                    di.url = domain['rooturl']
                print u'Added domain entry for {0}'.format(di.url)
                di.save()
                added = added + 1
            if options['tagverify'] and options['language'] != 'en':
                if not di.language_association and not di.uses_language_subdirs and not di.uses_language_query_parameter and not di.uses_langid:
                    di.language_association = options['language']
                    di.save()
                    langassoc = langassoc + 1
                    print u'Domain {0} marked as {1}'.format(di.url, options['language'])
            processed = processed + 1
            if processed >= max:
                break
        elapsed = timezone.now() - start
        print u'Processed {0} domains from {1} and added {2} new entries in {3} seconds and set {4} languages.'.format(processed, site_model, added, elapsed.total_seconds(), langassoc)
