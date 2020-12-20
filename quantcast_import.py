# -*- coding: utf-8 -*-

# Script to import Alexa top 1 million site ratings into the database.
# This file can be obtained from:
#
# http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

import os
import sys
#sys.path.append(settings.APP_DIRECTORY)
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
import wget
import zipfile
django.setup()

#import optparse
from dir.models import *
from dir.utils import *
from django.db import connection
import csv

def LoadQuantcastFile(filename):
    added_to_pending = 0
    added_domains = 0
    blocked_domains = 0
    updated_domains = 0
    crawl_needed = []
    crawl_blocked = []
    skipped = []
    processed = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        # Set all Quantcast results as old.
        print('Marking all previous quantcast rank data as outdated.')
        cursor = connection.cursor()
        cursor.execute('UPDATE dir_domaininfo SET quantcast_outdated = true WHERE quantcast_outdated = false;')
        print('Updating ranks.')
        for row in reader:
            if (len(row) > 1) and ((row[0] == 'Rank') or (row[0] == 'Hidden profile')):
                continue
            if len(row) == 2:
                print('Domain ' + row[1] + ' ranks ' + row[0])
                root = GetRootDomain(row[1])
                if UpdateQuantcastRank(row[1], row[0]):
                    if not CanCrawlUrl(row[1]):
                        print('Domain {0} cannot be crawled, not adding to crawl needed'.format(row[1]))
                        crawl_blocked.append(row[1])
                    else:
                        crawl_needed.append(row[1])
                processed.append(row[1])
    with open("quantcast_new.txt", 'w') as outfile:
        for item in crawl_needed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("quantcast_skipped.txt", 'w') as outfile:
        for item in skipped:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("quantcast_blocked.txt", 'w') as outfile:
        for item in crawl_blocked:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("quantcast_processed.txt", 'w') as outfile:
        for item in processed:
            outfile.write('%s\n' % item)
        outfile.close()
    print('Updated ' + str(len(processed)) + ' domains. ' + str(len(crawl_needed)) + ' need to be crawled.')

# /usr/bin/wget -O $MYFILENAME https://ak.quantcast.com/quantcast-top-sites.zip
if not os.path.isfile('Quantcast-Top-Million.txt'):
    print('File Quantcast-Top-Million.txt does not exist. Retrieving.')
    filename = wget.download('https://ak.quantcast.com/quantcast-top-sites.zip')
    if not filename:
        print('Failed to download Quantcast file.')
        exit(0)
    zip_ref = zipfile.ZipFile('./quantcast-top-sites.zip', 'r')
    zip_ref.extractall('.')
    zip_ref.close()
LoadQuantcastFile('Quantcast-Top-Million.txt')
