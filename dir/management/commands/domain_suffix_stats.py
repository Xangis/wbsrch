# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import DomainSuffix
from dir.utils import CalculateDomainSuffixStats
from tlds import tld_set


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-a', '--after', default=None, action='store', dest='after', help='Update only AFTER this extension, alphabetically. If not specified, all are updated. Period is optional.')
        parser.add_argument('-t', '--tld', default=None, action='store', dest='tld', help='Update ONLY this TLD. If not specified, all are updated.')
        parser.add_argument('-o', '--onlynew', default=None, action='store_true', dest='onlynew', help='Calculate ONLY domains that have never been calculated.')

    def handle(self, *args, **options):
        counts = []
        tlds = sorted(tld_set)
        tld = options.get('tld', None)
        after = options.get('after', None)
        onlynew = options.get('onlynew', False)
        if tld:
            if tld.startswith('.'):
                tld = tld[1:]
            tlds = [tld, ]
        if after:
            if after.startswith('.'):
                after = after[1:]
        for tld in tlds:
            if after and tld < after:
                continue
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
