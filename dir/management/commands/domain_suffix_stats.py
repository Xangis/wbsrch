# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from dir.models import language_list, DomainInfo, SiteInfo, BlockedSite, DomainSuffix
from dir.utils import GetSiteInfoModelFromLanguage
from tlds import tld_set

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-t', '--tld', default='all', action='store', type='string', dest='tld', help='Update ONLY this TLD. If not specified, all are updated.'),
    )

    def handle(self, *args, **options):
        counts = []
        tlds = tld_set
        tld = options.get('tld', None)
        if tld:
            if tld.startswith('.'):
                tld = tld[1:]
            tlds = [tld,]
        for tld in tlds:
            tldwithdot = '.{0}'.format(tld)
            print('Checking {0}'.format(tldwithdot))
            num_domains = DomainInfo.objects.filter(url__endswith=tldwithdot).values('url').count()
            print('Domains ending in {0}: {1}'.format(tldwithdot, num_domains))
            num_domains_with_pages = 0
            for lang in language_list:
                site_model = GetSiteInfoModelFromLanguage(lang)
                with_pages = site_model.objects.filter(rooturl__endswith=tldwithdot).values('rooturl').distinct().count()
                if with_pages > 0:
                    print('Num domains ending in {0} with pages in {1} index: {2}'.format(tldwithdot, lang, with_pages))
                    num_domains_with_pages += with_pages
            print('Total num domains ending in {0} with pages in all indexes: {1}'.format(tldwithdot, num_domains_with_pages))
            num_blocked_domains = BlockedSite.objects.filter(url__endswith=tldwithdot).values('url').count()
            print('Num domains ending in {0} that are blocked: {1}'.format(tldwithdot, num_blocked_domains))
            if num_domains_with_pages > 0:
                ratio = (num_blocked_domains * 100.0) / num_domains_with_pages
                print('Ratio of blocked domains to domains with pages in index: {0}%'.format(ratio))
            else:
                ratio = 0
                print('No domains ending in {0} in index, cannot calculate ratio.'.format(tldwithdot))
            counts.append((tld, num_domains, num_domains_with_pages, num_blocked_domains, ratio))
            try:
                suffix = DomainSuffix.objects.get(extension=tldwithdot)
            except ObjectDoesNotExist:
                suffix = DomainSuffix()
                suffix.extension = tldwithdot
            suffix.num_known = num_domains
            suffix.num_crawled = num_domains_with_pages
            suffix.num_blocked = num_blocked_domains
            suffix.blocked_to_crawled_ratio = ratio
            suffix.save()
        print(counts)
