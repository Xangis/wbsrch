# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=5, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=5)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-j', '--justthisurl', default=None, action='store', type='string', dest='justthisurl', help='Calculate only for this url.'),
        make_option('-r', '--recalculate', default=False, action='store_true', dest='recalculate', help='Update already-populated domains instead of uncounted (default=False)'),
        make_option('-p', '--popularity', default=False, action='store_true', dest='popularity', help='Sort by popularity before processing. (default=False)'),
        make_option('-u', '--urlcounts', default=False, action='store_true', dest='urlcounts', help='Update domain URL counts, not link counts.. (default=False)'),
        make_option('-k', '--keywordcounts', default=False, action='store_true', dest='keywordcounts', help='Update domain URL counts, not link counts.. (default=False)'),
        make_option('-t', '--total', default=False, action='store_true', dest='total', help='After running, show the total number of domains without number of links calculated. (defaul=False)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        sleeptime = options['sleep']
        urlcounts = options.get('urlcounts', False)
        total = options.get('total', False)
        keywordcounts = options.get('keywordcounts', False)
        if options.get('justthisurl', None):
            domains = DomainInfo.objects.filter(url=options['justthisurl'])
        elif options['recalculate']:
            if urlcounts:
                domains = DomainInfo.objects.filter(num_urls_last_updated__isnull=False).order_by('num_urls_last_updated')
            elif keywordcounts:
                domains = DomainInfo.objects.filter(num_keywords_ranked_last_updated__isnull=False).order_by('num_keywords_ranked_last_updated')
            else:
                domains = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=False).order_by('domains_linking_in_last_updated')
        else:
            if urlcounts:
                domains = DomainInfo.objects.filter(num_urls_last_updated__isnull=False)
            elif keywordcounts:
                domains = DomainInfo.objects.filter(num_keywords_ranked_last_updated__isnull=False)
            else:
                domains = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True)
        if options['popularity']:
            domains = domains.order_by('alexa_rank')
        domains = domains[options['offset']:options['offset']+options['max']]
        for domain in domains:
            # PROBLEM: For the number of URLs crawled and number of keywords ranked, we have to take language into account.
            # It's not enough to just count the number of URLs and their ranks for the main language, because subdomain, infix,
            # urlparam, and langid domains may rank and have URLs in multiple language indexes.
            #
            # To do this right, we may need to store a dictionary containing counts for each language along with a site-wide total.
            if urlcounts:
                num_urls = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} urls crawled for {1}'.format(num_urls, domain.url)
                domain.num_urls = num_urls
                domain.num_urls_last_updated = timezone.now()
            elif keywordcounts:
                num_keywords_ranked = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} keywords ranked for {1}'.format(num_keywords_ranked, domain.url)
                domain.nuM_keywords_ranked = num_keywords_ranked
                domain.num_keywords_ranked_last_updated = timezone.now()
            else:
                num_domains_linking_in = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} incoming links for {1}'.format(num_domains_linking_in, domain.url)
                domain.domains_linking_in = num_domains_linking_in
                domain.domains_linking_in_last_updated = timezone.now()
            domain.save()
            if sleeptime:
                time.sleep(sleeptime)
        updated = domains.count()
        elapsed = timezone.now() - start
        if total:
            nototal = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True).count()
            print u'{0} domains still do not have link count information.'.format(nototal)
        print u'{0} domains updated in {1} seconds.'.format(updated, elapsed.total_seconds())
