# This is a script to iterate through all the excluded domains and make sure
# that all URLs for them are blocked.

import os
import sys
import time
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'


for exclude in ExcludedSite.objects.all():
    print('Removing ' + exclude.url)
    RemoveURLsForDomain(exclude.url)
    time.sleep(0.05)
