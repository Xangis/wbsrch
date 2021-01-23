# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

# Script to import Majestic top 1 million site ratings into the database.
# This file can be obtained from:
#
# http://downloads.majestic.com/domcop_million.csv

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
import wget
import zipfile
django.setup()

from dir.models import *
from dir.utils import *
from django.db import connection
import csv


def LoadDomcopFile(filename, skip):
    crawl_needed = []
    crawl_blocked = []
    processed = []
    first = True
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if skip:
            print('Skip is set. Not marking previous Domcop rank data as outdated.')
        else:
            # Set all Domcop results as old.
            print('Marking all previous Domcop rank data as outdated.')
            cursor = connection.cursor()
            cursor.execute('UPDATE dir_domaininfo SET domcop_pagerank_outdated = true WHERE domcop_pagerank_outdated = false;')
        print('Updating ranks.')
        for row in reader:
            if first:
                first = False
                continue
            # "Rank","Domain","Open Page Rank"
            # "1","fonts.googleapis.com","10.00"
            # "2","facebook.com","10.00"
            # Column 0 = rank.
            # Column 1 = domain.
            # Column 2 = pagerank.
            if len(row) >= 3:
                print('Domain {0} ranks {1}'.format(row[1], row[0]))
                GetRootDomain(row[1])
                # UpdateDomcopRank(domain_name, rank, pagerank)
                if UpdateDomcopRank(row[1], row[0], row[2]):
                    if not CanCrawlUrl(row[2]):
                        print('Domain {0} cannot be crawled, not adding to crawl needed'.format(row[1]))
                        crawl_blocked.append(row[1])
                    else:
                        crawl_needed.append(row[1])
                processed.append(row[1])
    with open("domcop_new.txt", 'w') as outfile:
        for item in crawl_needed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("domcop_blocked.txt", 'w') as outfile:
        for item in crawl_blocked:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("domcop_processed.txt", 'w') as outfile:
        for item in processed:
            outfile.write('%s\n' % item)
        outfile.close()
    print('Updated {0} domains. {1} need to be crawled.'.format(processed, len(crawl_needed)))


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-s', '--skipoutdated', default=False, action='store_true', dest='skip', help='Skips the step of marking all existing entries as outdated.')

    def handle(self, *args, **options):
        skip = options['skip']
        # /usr/bin/wget -nv -O $MYFILENAME https://www.domcop.com/files/top/top10milliondomains.csv.zip
        if not os.path.isfile('top10milliondomains.csv'):
            print('File top10milliondomains.csv does not exist. Retrieving.')
            filename = wget.download('https://www.domcop.com/files/top/top10milliondomains.csv.zip')
            if not filename:
                print('Failed to download Domcop file.')
                exit(0)
            zip_ref = zipfile.ZipFile('./top10milliondomains.csv.zip', 'r')
            zip_ref.extractall('.')
            zip_ref.close()
        LoadDomcopFile('top10milliondomains.csv', skip)
