# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from dir.models import language_list, DomainInfo, SiteInfo, BlockedSite, DomainSuffix
from dir.utils import CalculateDomainSuffixStats
from tlds import tld_set

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-t', '--tld', default=None, action='store', type='string', dest='tld', help='Update ONLY this TLD. If not specified, all are updated.'),
        make_option('-o', '--onlynew', default=None, action='store_true', dest='onlynew', help='Calculate ONLY domains that have never been calculated.'),
    )

    def handle(self, *args, **options):
        counts = []
        tlds = sorted(tld_set)
        tld = options.get('tld', None)
        onlynew = options.get('onlynew', False)
        if tld:
            if tld.startswith('.'):
                tld = tld[1:]
            tlds = [tld,]
        for tld in tlds:
            tldwithdot = '.{0}'.format(tld)
            if onlynew:
                try:
                    suffix = DomainSuffix.objects.get(extension=tldwithdot)
                    print('{0} already exists, skipping'.format(tldwithdot))
                    continue
                except ObjectDoesNotExist:
                    pass
            suffix = CalculateDomainSuffixStats(tldwithdot)
            counts.append((tld, suffix.num_known, suffix.num_crawled, suffix.num_blocked, suffix.blocked_to_crawled_ratio))
        print(counts)
