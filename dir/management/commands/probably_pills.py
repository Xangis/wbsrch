# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from dir.models import DomainInfo, PageLink, BlockedSite, SiteInfo
from dir.utils import RemoveURLsForDomain


class Command(BaseCommand):
    help = "Checks link and block data to create a list of domains that are probably pills."

    def add_arguments(self, parser):
        parser.add_argument('-m', '--max', default=100000000, action='store', type=int, dest='max', help='Max number of links from domain to check. (default=10000000)')
        parser.add_argument('-s', '--sleep', default=0, action='store', type=int, dest='sleep', help='Time to sleep between domain checks. (default=0)')
        parser.add_argument('-n', '--min', default=0, action='store', type=int, dest='min', help='Minimum number of links from domains to check. (default=0)')

    def handle(self, *args, **options):
        start = timezone.now()
        max = options.get('max', 10000000)
        min = options.get('min', 0)
        domains = BlockedSite.objects.filter(reason=5).order_by('url')
        pillsdict = {}
        ipsdict = {}
        print(min)
        print(max)
        print(len(domains))
        print('Checking domains with between {1} and {2} links. Retrieved {0}.'.format(len(domains), min, max))
        for domain in domains:
            links = PageLink.objects.filter(rooturl_destination=domain.url)
            for link in links:
                if link.rooturl_source in pillsdict:
                    pillsdict[link.rooturl_source] = pillsdict[link.rooturl_source] + 1
                else:
                    pillsdict[link.rooturl_source] = 1
            try:
                dinfo = DomainInfo.objects.get(url=domain)
                if dinfo.robots_ip:
                    if dinfo.robots_ip in ipsdict:
                        ipsdict[dinfo.robots_ip] += 1
                    else:
                        ipsdict[dinfo.robots_ip] = 1
            except ObjectDoesNotExist:
                pass
        pillsdict = sorted(pillsdict.items(), key=lambda item: item[1], reverse=True)
        print('{0} domains were found linking to these {1} sites blocked as pills.'.format(len(pillsdict), len(domains)))
        processed = 0
        for domainurl in pillsdict:
            processed = processed + 1
            if processed % 1000 == 0:
                print('Processed {0}.'.format(processed))
            if (domainurl[1] < min) or (domainurl[1] > max):
                continue
            pages = SiteInfo.objects.filter(rooturl=domainurl[0])
            num_pages = len(pages)
            print('{0} has {1} outbound links and {2} pages.'.format(domainurl[0], domainurl[1], num_pages))
            for page in pages:
                try:
                    print('Url: {0}, Title: {1}'.format(page.url, page.pagetitle))
                except Exception:
                    print('Url: {0}, Title: unprintable'.format(page.url))
            try:
                BlockedSite.objects.get(url=domainurl[0])
                print('PROBLEM: Domain {0} is blocked but still has links to other sites in database.'.format(domainurl[0]))
                continue
            except ObjectDoesNotExist:
                pass
            prompt = 'Delete? [y/n/q] '
            rinput = input(prompt).lower()
            if rinput == 'q':
                exit(0)
            elif rinput == 'n':
                continue
            elif rinput == 'y':
                print('Deleting {0}'.format(domainurl[0]))
                bsite = BlockedSite()
                bsite.url = domainurl[0]
                bsite.reason = 5
                bsite.save()
                RemoveURLsForDomain(domainurl[0])
        elapsed = timezone.now() - start
        print('IPs of Blocked Pills Sites: {0}'.format(ipsdict))
        print('Task completed in {0} seconds.'.format(elapsed.total_seconds()))
