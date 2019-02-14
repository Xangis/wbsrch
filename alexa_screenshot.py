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

import StringIO
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
import signal
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

WIDTH = 1280
HEIGHT = 800
SMALLWIDTH = 320
SMALLHEIGHT = 200

def TakeScreenshot(url):
    print('Screenshotting domain ' + url)
    caps = dict(DesiredCapabilities.PHANTOMJS)
    caps["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (compatible; WbSrch/1.1 +https://wbsrch.com)"
    driver = webdriver.PhantomJS(executable_path="node_modules/phantomjs/bin/phantomjs", desired_capabilities=caps)
    driver.set_window_size(WIDTH, HEIGHT) # optional
    driver.get('https://{0}'.format(url))
    screen = driver.get_screenshot_as_png()
    # Crop it back to the window size (it may be taller)
    box = (0, 0, WIDTH, HEIGHT)
    im = Image.open(StringIO.StringIO(screen))
    region = im.crop(box)
    region.save('screenshots/{0}.png'.format(url), 'PNG')
    size = SMALLWIDTH, SMALLHEIGHT
    region.thumbnail(size)
    region.save('screenshots/{0}.320px.png'.format(url), 'PNG')
    # Terminate phantomjs process. See: https://adiyatmubarak.wordpress.com/2017/03/29/python-fix-oserror-errno-9-bad-file-descriptor-in-selenium-using-phantomjs/
    driver.service.process.send_signal(signal.SIGTERM)
    try:
       driver.quit()
    except OSError:
       # We can still get these errors, but at least the phantomjs process will terminate.
       pass
    return False

def LoadAlexaFile(filename):
    added_to_pending = 0
    added_domains = 0
    screenshot_failed = []
    screenshot_succeeded = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Capture a screenshot for every domain.
        for row in reader:
            if len(row) == 2:
                #root = GetRootDomain(row[1])
                if not TakeScreenshot(row[1]):
                    print('Error screenshotting {0}'.format(row[1]))
                    screenhot_failed.append(row[1])
                    screenshot_succeeded.append(row[1])
                processed.append(row[1])
    with open("screenshot_failed.txt", 'w') as outfile:
        for item in screenshot_failed:
            outfile.write('%s\n' % item)
        outfile.close()
    with open("screenshot_succeeded.txt", 'w') as outfile:
        for item in screenshot_succeeded:
            outfile.write('%s\n' % item)
        outfile.close()
    print('Captured {0} domain screenshots. {1] failed to capture.'.format(len(screenshot_succeeded), len(screenshot_failed)))


TakeScreenshot('analytics.wbsrch.com')
TakeScreenshot('bloodlessmushroom.com')
TakeScreenshot('sashaandthechildren.com')
TakeScreenshot('rainwithoutend.com')
TakeScreenshot('emergencybrunch.com')
TakeScreenshot('orcfucker.com')
TakeScreenshot('toiletduckhunt.com')
TakeScreenshot('zetacentauri.com')
TakeScreenshot('xangis.com')
TakeScreenshot('stampscoinsnotes.com')
TakeScreenshot('freewavesamples.com')
TakeScreenshot('soundprogramming.net')
TakeScreenshot('silica-gel.org')
TakeScreenshot('bassguitarpro.com')
TakeScreenshot('guitarl.com')
TakeScreenshot('stats.wbsrch.com')
TakeScreenshot('maps.wbsrch.com')
TakeScreenshot('browser.wbsrch.com')
TakeScreenshot('wbsrch.com')
TakeScreenshot('news.wbsrch.com')
exit(0)

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
