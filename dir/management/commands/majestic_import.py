# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

# Script to import Majestic top 1 million site ratings into the database.
# This file can be obtained from:
#
# http://downloads.majestic.com/majestic_million.csv

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
import wget
django.setup()

from dir.utils import GetRootDomain, UpdateMajesticRank, CanCrawlUrl
from django.db import connection
import csv


def LoadAlexaFile(filename, skip):
    crawl_needed = []
    crawl_blocked = []
    processed = []
    first = True
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if skip:
            print('Skip is set. Not marking previous Majestic data as outdated.')
        else:
            # Set all Majestic results as old.
            print('Marking all previous Majestic rank data as outdated.')
            cursor = connection.cursor()
            cursor.execute('UPDATE dir_domaininfo SET majestic_outdated = true WHERE majestic_outdated = false;')
        print('Updating ranks.')
        # GlobalRank,TldRank,Domain,TLD,RefSubNets,RefIPs,IDN_Domain,IDN_TLD,PrevGlobalRank,PrevTldRank,PrevRefSubNets,PrevRefIPs
        # 1,1,google.com,com,492996,3120968,google.com,com,1,1,491732,3118138
        # 2,2,facebook.com,com,477119,3140009,facebook.com,com,2,2,475930,3138386
        # 3,3,youtube.com,com,437532,2566963,youtube.com,com,3,3,436594,2565805
        for row in reader:
            if first:
                first = False
                continue
            # Column 0 = rank.
            # Column 2 = domain.
            if len(row) >= 3:
                print('Domain ' + row[2] + ' ranks ' + row[0])
                GetRootDomain(row[2])
                if UpdateMajesticRank(row[2], row[0], row[4]):
                    if not CanCrawlUrl(row[2]):
                        print('Domain {0} cannot be crawled, not adding to crawl needed'.format(row[2]))
                        crawl_blocked.append(row[2])
                    else:
                        crawl_needed.append(row[2])
                processed.append(row[2])
    with open("majestic_new.txt", 'w') as outfile:
        for item in crawl_needed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("majestic_blocked.txt", 'w') as outfile:
        for item in crawl_blocked:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("majestic_processed.txt", 'w') as outfile:
        for item in processed:
            outfile.write('%s\n' % item)
        outfile.close()
    print('Updated ' + str(len(processed)) + ' domains. ' + str(len(crawl_needed)) + ' need to be crawled.')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-s', '--skipoutdated', default=False, action='store_true', dest='skip', help='Skips the step of marking all existing entries as outdated.')

    def handle(self, *args, **options):
        skip = options['skip']
        if not os.path.isfile('majestic_million.csv'):
            print('File majestic_million.csv does not exist. Retrieving.')
            filename = wget.download('http://downloads.majestic.com/majestic_million.csv')
            if not filename:
                print('Failed to download Majestic file.')
                exit(0)
        LoadAlexaFile('majestic_million.csv', skip)
