# This is a script to iterate through all the excluded domains and make sure
# that all URLs for them are blocked.

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

import time
#import optparse
from urllib.parse import urlparse
from dir.models import *
from django.db.utils import DatabaseError
from django.db import connection
from django.utils.timezone import utc
from django.core.exceptions import ValidationError
from django.db import transaction
import datetime
import csv

for exclude in ExcludedSite.objects.all():
    print('Removing ' + exclude.url)
    RemoveURLsForDomain(exclude.url)
    time.sleep(0.05)
