# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from dir.models import DomainInfo, PageLink
import time
import codecs


class Command(BaseCommand):
    help = "This command updates domain metadata. It's used for updating domain link counts and domain keyword counts."

    def add_arguments(self, parser):
        parser.add_argument('-m', '--max', default=100000, action='store', type=int, dest='max', help='Max number of domains to update. (default=100000)')
        parser.add_argument('-s', '--sleep', default=0, action='store', type=int, dest='sleep', help='Time to sleep between domain queries. (default=0)')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)')
        parser.add_argument('-j', '--justthisurl', default=None, action='store', dest='justthisurl', help='Calculate only for this url.')
        parser.add_argument('-r', '--recalculate', default=False, action='store_true', dest='recalculate', help='Update already-populated domains instead of uncounted (default=False)')
        parser.add_argument('-p', '--popularity', default=False, action='store_true', dest='popularity', help='Sort by popularity before processing. (default=False)')
        parser.add_argument('-u', '--urlcounts', default=False, action='store_true', dest='urlcounts', help='Update domain URL counts, not link counts.. (default=False)')
        parser.add_argument('-k', '--keywordcounts', default=False, action='store_true', dest='keywordcounts', help='Update domain URL counts, not link counts.. (default=False)')
        parser.add_argument('-t', '--total', default=False, action='store_true', dest='total', help='After running, show the total number of domains without number of links calculated. (defaul=False)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load domain list from specified file.')

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
        elif options['file']:
            filename = options['file']
            domains = []
            numloaded = 0
            print('Loading domains to update from file: {0}'.format(filename))
            f = open(filename, 'rb')
            reader = codecs.getreader('utf8')(f)
            for line in reader.readlines():
                line = line.strip()
                numloaded = numloaded + 1
                try:
                    domain = DomainInfo.objects.get(url=line)
                    domains.append(domain)
                except ObjectDoesNotExist:
                    # Create domain if not found. This could be problematic if we have a file full of garbage text.
                    print('Domain {0} not found, creating before update.'.format(line))
                    domain = DomainInfo()
                    domain.url = line
                    domain.save()
                    domains.append(domain)
            print('{0} domains loaded from file {1}.'.format(numloaded, filename))
        else:
            if urlcounts:
                domains = DomainInfo.objects.filter(num_urls_last_updated__isnull=False)
            elif keywordcounts:
                domains = DomainInfo.objects.filter(num_keywords_ranked_last_updated__isnull=False)
            else:
                domains = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True)
        if options['popularity']:
            domains = domains.order_by('alexa_rank')
        domains = domains[options['offset']:options['offset'] + options['max']]
        for domain in domains:
            # PROBLEM: For the number of URLs crawled and number of keywords ranked, we have to take language into account.
            # It's not enough to just count the number of URLs and their ranks for the main language, because subdomain, infix,
            # urlparam, and langid domains may rank and have URLs in multiple language indexes.
            #
            # To do this right, we may need to store a dictionary containing counts for each language along with a site-wide total.
            if urlcounts:
                num_urls = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print('{0} urls crawled for {1}'.format(num_urls, domain.url))
                domain.num_urls = num_urls
                domain.num_urls_last_updated = timezone.now()
            elif keywordcounts:
                num_keywords_ranked = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print('{0} keywords ranked for {1}'.format(num_keywords_ranked, domain.url))
                domain.nuM_keywords_ranked = num_keywords_ranked
                domain.num_keywords_ranked_last_updated = timezone.now()
            else:
                num_domains_linking_in = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print('{0} incoming links for {1}'.format(num_domains_linking_in, domain.url))
                domain.domains_linking_in = num_domains_linking_in
                domain.domains_linking_in_last_updated = timezone.now()
            domain.save()
            if sleeptime:
                time.sleep(sleeptime)
        updated = len(domains)
        elapsed = timezone.now() - start
        if total:
            nototal = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True).count()
            print('{0} domains still do not have link count information.'.format(nototal))
        print('{0} domains updated in {1} seconds.'.format(updated, elapsed.total_seconds()))
