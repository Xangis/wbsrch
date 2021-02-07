# -*- coding: utf-8 -*-
from django.db import connections
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import SearchLog, PendingIndex, language_list
from dir.utils import AddPendingTerm, GetIndexModelFromLanguage, GetRootUrl
import codecs


class Command(BaseCommand):
    help = """
    Two-way sync with master indexes server.
    """
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default='en', action='store', dest='language', help='Language to use for pending indexes (default=en).')
        parser.add_argument('-d', '--domains', default=False, action='store_true', dest='domains', help='Process file as a domain list and print the domains that need to be crawled. Redundant with -p since it only prints (default=no).')
        parser.add_argument('-p', '--print', default=False, action='store_true', dest='print', help='Just print the terms that are not indexed to the screen, do not create pending terms. (default=no).')
        parser.add_argument('-n', '--noindividual', default=False, action='store_true', dest='noindividual', help='Make sure individual words of a phrase are not indexed (default=False)')
        parser.add_argument('-m', '--maxwords', default=100000000, action='store', type=int, dest='maxwords', help='Max number of terms to index. (default=100000000)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load term list from specified file.')

    def handle(self, *args, **options):
        for language in language_list:
            if language != 'en':
                # TODO: implement other languages.
                continue
            with connections['live_indexes'].cursor() as cursor:
                last_log = SearchLog.objects.all().order_by('-id').first()
                newest_date = last_log.last_search
                query = 'SELECT * FROM dir_searchlog WHERE last_search > {0} ORDER BY last_search'.format(newest_date)
                cursor.execute(query)
                for item in cursor.dictfetchall():
                    print(item)
                query = 'SELECT * FROM dir_indexstats ORDER BY date DESC LIMIT 1'
                result = cursor.fetchone()
                last_pendingindex = PendingIndex.objects.all().order_by('-date_added').first()
                newest_date = last_pendingindex.date_added
                query = 'SELECT * FROM dir_pendingindex WHERE date_added > {0} ORDER BY date_added'.format(newest_date)
                for item in cursor.dictfetchall():
                    print(item)
