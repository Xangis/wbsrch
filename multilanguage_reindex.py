from subprocess import call
import time

import os
import sys
from zetaweb import settings
sys.path.append(settings.APP_DIRECTORY)
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

from dir.views import language_list

while True:
    for language in language_list:
        if language is 'en':
            continue
        # Reindex one old term for every 10 new terms being indexed.
        # We do things in larger batches than the en daemon in order to
        # take advantage of caching (which may or may not make a difference,
        # we haven't benchmarked anything).
        call(['python', 'manage.py', 'index', '-r', '-m', '20', '-s', '1', '-o', '100', '-l', language])
        # Wait a few seconds between cycles.
        time.sleep(1)
    
