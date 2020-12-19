# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink, BlockedSite, SiteInfo
from dir.utils import PornBlock
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


class Command(BaseCommand):
    help = "Checks link and block data to create a list of domains that are probably porn."
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=100000000, action='store', type='int', dest='max', help='Max number of links from domain to check. (default=10000000)'),
        make_option('-s', '--sleep', default=0, action='store', type='int', dest='sleep', help='Time to sleep between domain checks. (default=0)'),
        make_option('-n', '--min', default=0, action='store', type='int', dest='min', help='Minimum number of links from domains to check. (default=0)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        max = options.get('max', 10000000)
        min = options.get('min', 0)
        domains = BlockedSite.objects.filter(reason=4).order_by('url')
        porndict = {}
        print('Checking domains with between {1} and {2} links. Retrieved {0}.'.format(len(domains), min, max))
        for domain in domains:
            links = PageLink.objects.filter(rooturl_destination=domain.url)
            for link in links:
                if link.rooturl_source in porndict:
                    porndict[link.rooturl_source] = porndict[link.rooturl_source] + 1
                else:
                    porndict[link.rooturl_source] = 1
        porndict = sorted(porndict.items(), key=lambda item: item[1], reverse=True)
        print('{0} domains were found linking to these {1} sites blocked as porn.'.format(len(porndict), len(domains)))
        processed = 0
        for domainurl in porndict:
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
                except:
                    print('Url: {0}, Title: unprintable'.format(page.url))
            try:
                blocked = BlockedSite.objects.get(url=domainurl[0])
                print('PROBLEM: Domain {0} is blocked but still has links to other sites in database.'.format(domainurl[0]))
                continue
            except:
                pass
            prompt = 'Delete? [y/n/v/q] '
            input = raw_input(prompt.encode(sys.stdout.encoding)).lower()
            if input == 'q':
                exit(0)
            elif input == 'n':
                continue
            elif input == 'v':
                domain = DomainInfo.objects.get(url=domainurl[0])
                domain.verified_notporn = True
                domain.save()
                continue
            elif input == 'y':
                PornBlock(url=domainurl[0])
        elapsed = timezone.now() - start
        print('Task completed in {0} seconds.'.format(elapsed.total_seconds()))
