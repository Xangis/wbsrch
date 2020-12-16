# This is a script to iterate through all the domains that use a language in the url,
# like "host.com/de/index.htm" and make sure that all URLs for them are moved to the
# correct language.

import os
import sys
sys.path.append('/var/django/wbsrch/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetaweb.settings'

import time
#import optparse
from dir.models import *
from dir.utils import MoveSiteTo
from dir.language import GetInfixLanguage, InvalidLanguageException, GetUrlParameterLanguage
from django.db.utils import DatabaseError
from django.db import connection
from django.utils.timezone import utc
from django.core.exceptions import ValidationError
from django.db import transaction
import datetime
import csv

# Required now that we're on Django 1.7. Otherwise we get "Models aren't loaded yet" error.
import django
django.setup()

totalurls = 0
totalmoved = 0
notfound = 0
invalid = 0
isroot = 0
moved = {}
deleted = {}
notmatched = []

def ProcessParametersForDomain(domain):
    global totalurls
    global totalmoved
    global notfound
    global invalid
    global isroot
    global moved
    global deleted
    global notmatched
    urls = SiteInfo.objects.filter(rooturl=domain.url)
    url_count = urls.count()
    totalurls += url_count
    if url_count > 0:
        print('Found: ' + str(url_count) + u' for ' + domain.url)
    for url in urls:
        if url == (u'http://' + url.rooturl) or url == (u'http://' + url.rooturl):
            isroot = isroot + 1
        try:
            if domain.uses_language_subdirs:
                result = GetInfixLanguage(url.url)
                #print u'Infix language for {0} is: {1}'.format(url.url, result)
            elif domain.uses_language_query_parameter:
                result = GetUrlParameterLanguage(url.url)
                #print u'URL Parameter language for {0} is: {1}'.format(url.url, result)
            if result and result != u'en':
                # Move to the new language, but don't tag the domain as that language or
                # as uses language infix because they domain is already set properly.
                MoveSiteTo(url, result, False, False)
                if result in moved:
                    moved[result] = moved[result] + 1
                else:
                    moved[result] = 1
                totalmoved = totalmoved + 1
            elif result == u'en':
                continue
            else:
                print('No result for URL {0}'.format(url))
                notmatched.append(url)
                notfound = notfound + 1
        except InvalidLanguageException as e:
            print('URL {0} has invalid language {1} and will be deleted.'.format(url, e.message))
            if e.message in deleted:
                deleted[e.message] = deleted[e.message] + 1
            else:
                deleted[e.message] = 1
            invalid = invalid + 1
            url.delete()

for domain in DomainInfo.objects.filter(uses_language_subdirs=True).order_by('url'):
    ProcessParametersForDomain(domain)
for domain in DomainInfo.objects.filter(uses_language_query_parameter=True).order_by('url'):
    ProcessParametersForDomain(domain)
print('Moved {0} urls to other languages out of a possible {1}. {2} not found, {3} blocked languages, {4} ignored root URLs.'.format(totalmoved, totalurls, notfound, invalid, isroot))
for lang in moved.keys():
    print('Moved ' + str(moved[lang]) + u' to language ' + lang)
for lang in deleted.keys():
    print('Deleted ' + str(deleted[lang]) + u' for language ' + lang)
with open("unmatched_infixes.txt", 'w') as outfile:
    for item in notmatched:
        outfile.write('%s\n' % item)
    outfile.close()

