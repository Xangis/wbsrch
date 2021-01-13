# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import *
from dir.utils import *
import csv


def LoadExcludedSiteFile(filename):
    processed = 0
    added = 0
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # url,reason,detailedreason,id,exclude_subdomains
        # dushu.qq.com,8,Chinese language site.,74,f
        first = True
        for row in reader:
            if first:
                first = False
                continue
            processed += 1
            if len(row) == 5:
                domain = row[0].strip()
                print('Domain = ' + domain + ', reason = ' + row[1] + ', details = ' + row[2], ', block subdomains = ' + row[4])
                try:
                    BlockedSite.objects.get(url=domain)
                except ObjectDoesNotExist:
                    print('Adding new excluded site entry.')
                    site = BlockedSite()
                    site.url = domain
                    site.reason = int(row[1])
                    site.detailedreason = row[2]
                    if row[4] == 't':
                        site.exclude_subdomains = True
                    else:
                        site.exclude_subdomains = False
                    site.save()
                    added += 1
    print('Processed {0} blocked sites. {1} were newly removed.'.format(processed, added))


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        LoadExcludedSiteFile('excluded_sites.csv')
