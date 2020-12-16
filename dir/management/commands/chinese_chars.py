
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo
from dir.utils import GetSiteInfoModelFromLanguage
import time
import re

class Command(BaseCommand):
    help = "Analyzes page titles looking for Chinese characters and prints a list of domains that are likely Chinese"

    option_list = BaseCommand.option_list + (
        #make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        #make_option('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.'),
        #make_option('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.'),
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for domains (default=en). It is dumb to use not english because if a domain is in another table, it has been categorized and has a domain info.'),
        #make_option('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=15, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=15)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-t', '--threshold', default=0, action='store', type='int', dest='threshold', help='Min threshold required to count. (default=1, max=4)'),
        #make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),

        # TODO: Make an option to fill in nulls vs update already-queried domains.
    )

    def handle(self, *args, **options):
        site_model = GetSiteInfoModelFromLanguage(options['language'])
        max = options['max']
        offset = options['offset']
        threshold = options['threshold']
        pages = site_model.objects.all().values('pagetitle', 'pagefirstheadtag', 'pagefirsth2tag', 'pagefirsth3tag', 'id', 'rooturl')[offset:offset+max]
        processed = 0
        added = 0
        printed = 0
        domains = {}

        for page in pages:
            # print page
            id = page.get('id')
            rooturl = page.get('rooturl')
            title = page.get('pagetitle', None)
            if title:
                for n in re.findall(u'[\u4e00-\u9fff]+', title):
                    # print 'Chinese stuff found in site ID {0} root {1}:'.format(id, rooturl)
                    # print title
                    if domains.has_key(rooturl):
                        domains[rooturl] = domains[rooturl] + 1
                    else:
                        domains[rooturl] = 1
                    break
            pagefirstheadtag = page.get('pagefirstheadtag', None)
            if pagefirstheadtag:
                for n in re.findall(r'[\u4e00-\u9fff]+', pagefirstheadtag):
                    # print 'Chinese stuff found in site ID {0} root {1}:'.format(id, rooturl)
                    # print pagefirstheadtag
                    if domains.has_key(rooturl):
                        domains[rooturl] = domains[rooturl] + 1
                    else:
                        domains[rooturl] = 1
                    break
            pagefirsth2tag = page.get('pagefirsth2tag', None)
            if pagefirsth2tag:
                for n in re.findall(r'[\u4e00-\u9fff]+', pagefirsth2tag):
                    # print 'Chinese stuff found in site ID {0} root {1}:'.format(id, rooturl)
                    # print pagefirstheadtag
                    if domains.has_key(rooturl):
                        domains[rooturl] = domains[rooturl] + 1
                    else:
                        domains[rooturl] = 1
                    break
            pagefirsth3tag = page.get('pagefirsth3tag', None)
            if pagefirsth3tag:
                for n in re.findall(r'[\u4e00-\u9fff]+', pagefirsth3tag):
                    # print 'Chinese stuff found in site ID {0} root {1}:'.format(id, rooturl)
                    # print pagefirstheadtag
                    if domains.has_key(rooturl):
                        domains[rooturl] = domains[rooturl] + 1
                    else:
                        domains[rooturl] = 1
                    break
            processed = processed + 1
        results = sorted(domains.iteritems(), key=lambda item: item[1], reverse=False)
        for result in results:
            if result[1] >= threshold:
                print('{0} - {1}'.format(result[1], result[0]))
                printed = printed + 1
        print('Processed {0} urls and found {1} domains that are probably asian and {2} met print threshold.'.format(processed, len(results), printed))
