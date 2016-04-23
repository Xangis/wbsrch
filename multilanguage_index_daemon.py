from subprocess import call
import time

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

from dir.views import language_list

# Index ratio controls how quickly we cycle through terms for a language.

lang_index_counts = { 'lt': 5, 'lv': 3, 'is': 4, 'sw': 2, 'yo': 2, 'so': 2, 'wo': 2, 'ha': 2, 'rw': 2, 'sn': 2, 'ca': 2, 'cs': 15, 'fi': 13, 'el': 11, 'hu': 16, 'pl': 30, 'tr': 25, 'da': 7, 'et': 8, 'de': 18, 'no': 5, 'pt': 14, 'nl': 12, 'sk': 8, 'sl': 8, 'es': 20, 'sv': 8, 'hr': 15, 'cs': 16, 'it': 12, 'fr': 12 }

#language_list = ['en', 'de', 'fr', 'es', 'pl', 'it', 'nl', 'pt', 'tr', 'cs', 'ro', 'el', 'sv', 'da', 'hu', 'hr', 'sk', 'lt', 'no', 'fi', 'et', 'lv', 'sl', 'is', 'sw', 'yo', 'so', 'wo', 'ha', 'rw', 'sn', 'ca']

while True:
    for language in language_list:
        if language is 'en':
            continue
        # Reindex one old term for every 10 new terms being indexed.
        # We do things in larger batches than the en daemon in order to
        # take advantage of caching (which may or may not make a difference,
        # we haven't benchmarked anything).
        indexcount = lang_index_counts.get(language, 10)
        call(['python', 'manage.py', 'index', '-p', '-m', str(indexcount*2), '-s', '0', '-l', language])
        # Wait a few seconds between context switches
        time.sleep(1)
        call(['python', 'manage.py', 'index', '-r', '-m', str(indexcount*5), '-s', '0', '-l', language])
        # Wait a few seconds between cycles.
        time.sleep(1)
    
