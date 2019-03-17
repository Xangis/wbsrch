from subprocess import call
import time

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

from dir.views import language_list

while True:
    for x in range(1000, -20, -20):
        for language in language_list:
            if language is 'en':
                continue
            call(['python', 'manage.py', 'crawl', '-r', '-m', '20', '-s', '60', '-o', str(x), '-l', language])
