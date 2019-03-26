from subprocess import call
import time

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

from dir.views import language_list

# Based on a ratio vs French at 100,000 URLs wanting to recrawl 20 per round.
# Adjust accordingly as indexes evolve.
# Default is 1, which is appropriate for all small (<5k) indexes.
lang_crawl_counts = {
  'cs': 3, 'fr': 20, 'nl': 10, 'de': 50, 'hu': 2, 'it': 15, 'pl': 8, 'pt': 3, 'ro': 2, 'es': 14, 'sv': 7, 'tr': 5
}

while True:
    for x in range(100, -1, -1):
        for language in language_list:
            if language is 'en':
                continue
            lang_crawl_count = lang_crawl_counts.get(language, 1)
            call(['python', 'manage.py', 'crawl', '-r', '-m', str(lang_crawl_count), '-s', '1', '-o', str(x*lang_crawl_count), '-l', language])
