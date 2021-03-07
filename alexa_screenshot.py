# -*- coding: utf-8 -*-

# Take screenshots of the Alexa top 1 million URLs.
# This file can be obtained from:
#
# http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

# Install instructions
#
# npm install phantomjs
# sudo apt-get install libjpeg-dev
# pip install selenium pillow

import os
import sys
# sys.path.append(settings.APP_DIRECTORY)
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
import wget
import zipfile
django.setup()

import csv
from dir.utils import TakeScreenshot

WIDTH = 1280
HEIGHT = 800
SMALLWIDTH = 320
SMALLHEIGHT = 200


def LoadAlexaFile(filename):
    screenshot_failed = []
    screenshot_succeeded = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Capture a screenshot for every domain.
        rows = 0
        for row in reader:
            rows += 1
            if rows > 1000:
                break
            if len(row) == 2:
                # root = GetRootDomain(row[1])
                if not TakeScreenshot(row[1]):
                    print('Row {0}: Error screenshotting {1}'.format(rows, row[1]))
                    screenshot_failed.append(row[1])
                else:
                    screenshot_succeeded.append(row[1])
    with open("screenshot_failed.txt", 'w') as outfile:
        for item in screenshot_failed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("screenshot_succeeded.txt", 'w') as outfile:
        for item in screenshot_succeeded:
            outfile.write('%s\n' % item)
        outfile.close()
    print('Captured {0} domain screenshots. {1} failed to capture.'.format(len(screenshot_succeeded), len(screenshot_failed)))


# TakeScreenshot('analytics.wbsrch.com')
# TakeScreenshot('bloodlessmushroom.com')
# TakeScreenshot('sashaandthechildren.com')
# TakeScreenshot('rainwithoutend.com')
# TakeScreenshot('emergencybrunch.com')
# TakeScreenshot('orcfucker.com')
# TakeScreenshot('toiletduckhunt.com')
# TakeScreenshot('zetacentauri.com')
# TakeScreenshot('xangis.com')
# TakeScreenshot('stampscoinsnotes.com')
# TakeScreenshot('freewavesamples.com')
# TakeScreenshot('soundprogramming.net')
# TakeScreenshot('silica-gel.org')
# TakeScreenshot('bassguitarpro.com')
# TakeScreenshot('guitarl.com')
# TakeScreenshot('stats.wbsrch.com')
# TakeScreenshot('maps.wbsrch.com')
# TakeScreenshot('browser.wbsrch.com')
# TakeScreenshot('wbsrch.com')
# TakeScreenshot('news.wbsrch.com')
# exit(0)

if not os.path.isfile('top-1m.csv'):
    print('File top-1m.csv does not exist. Retrieving.')
    filename = wget.download('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    if not filename:
        print('Failed to download Alexa file.')
        exit(0)
    zip_ref = zipfile.ZipFile('./top-1m.csv.zip', 'r')
    zip_ref.extractall('.')
    zip_ref.close()
LoadAlexaFile('top-1m.csv')
