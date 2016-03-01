# -*- coding: utf-8 -*-

# Script to import Alexa top 1 million site ratings into the database.
# This file can be obtained from:
#
# http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

import os
import sys
from zetaweb import settings
#sys.path.append(settings.APP_DIRECTORY)
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
import wget
import zipfile
django.setup()

import time
#import optparse
from urlparse import urlparse
from dir.models import *
from dir.utils import *
from django.db.utils import DatabaseError
from django.db import connection
from django.utils.timezone import utc
from django.core.exceptions import ValidationError
from django.db import transaction
import datetime
import csv

def LoadAlexaFile(filename):
    processed = 0
    added_to_pending = 0
    added_domains = 0
    blocked_domains = 0
    updated_domains = 0
    crawl_needed = []
    crawl_blocked = []
    skipped = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Set all Alexa results as old.
        print u'Marking all previous alexa rank data as outdated.'
        cursor = connection.cursor()
        cursor.execute('UPDATE dir_domaininfo SET alexa_outdated = true WHERE alexa_rank > 0 and alexa_rank <= 1000000 AND alexa_outdated = false;')
        print u'Updating ranks.'
        for row in reader:
            if len(row) == 2:
                print('Domain ' + row[1] + ' ranks ' + row[0])
                root = GetRootDomain(row[1])
                # No longer skipping subdomains. Fill 'em in.
                #if root != row[1]:
                #    print('Domain {0} does not match {1}. Skipping'.format(root, row[1]))
                #    skipped.append(row[1])
                #    # Just because we didn't update the Alexa rank for a domain, doesn't mean we shouldn't
                #    # crawl it. For crawl purposes, treat it just like any other URL.
                #    if not CanCrawlUrl(row[1]):
                #        print('Domain {0} cannot be crawled, not adding to crawl needed'.format(row[1]))
                #        crawl_blocked.append(row[1])
                #    else:
                #        crawl_needed.append(row[1])
                #    continue
                if UpdateAlexaRank(row[1], row[0]):
                    if not CanCrawlUrl(row[1]):
                        print('Domain {0} cannot be crawled, not adding to crawl needed'.format(row[1]))
                        crawl_blocked.append(row[1])
                    else:
                        crawl_needed.append(row[1])
                processed = processed + 1
    with open("alexa_new.txt", 'w') as outfile:
        for item in crawl_needed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("alexa_skipped.txt", 'w') as outfile:
        for item in skipped:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("alexa_blocked.txt", 'w') as outfile:
        for item in crawl_blocked:
            outfile.write('%s\n' % item)
        outfile.close()
    print 'Updated ' + str(processed) + ' domains. ' + str(len(crawl_needed)) + ' need to be crawled.'

if not os.path.isfile('top-1m.csv'):
    print u'File top-1m.csv does not exist. Retrieving.'
    filename = wget.download('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    if not filename:
        print u'Failed to download Alexa file.'
        exit(0)
    zip_ref = zipfile.ZipFile('./top-1m.csv.zip', 'r')
    zip_ref.extractall('.')
    zip_ref.close()
LoadAlexaFile('top-1m.csv')
