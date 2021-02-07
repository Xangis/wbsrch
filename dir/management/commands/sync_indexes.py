# -*- coding: utf-8 -*-
from django.db import connections
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import SearchLog, PendingIndex, language_list, ChangelogItem, DomainSearchLog, IPSearchLog, DomainSuffix, IndexStats


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


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
                if last_log:
                    newest_date = last_log.last_search
                else:
                    newest_date = '2010-01-01'
                print('Last log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_searchlog WHERE last_search > '{0}' ORDER BY last_search LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer search logs:')
                # {'id': 5738100, 'keywords': 'belia', 'result_count': 250, 'last_search': datetime.datetime(2016, 5, 1, 19, 24, 50, 936411, tzinfo=<UTC>),
                # 'search_time': Decimal('0.07'), 'indexed': True, 'referer': None, 'ip': '207.46.13.40',
                # 'browserstring': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'is_bot': True, 'ip_country': 'US',
                # 'search_id': UUID('c4b1f620-3691-4d08-9b31-1233af606371')}
                for item in dictfetchall(cursor):
                    print(item)
                query = 'SELECT * FROM dir_indexstats ORDER BY date DESC LIMIT 1'
                result = cursor.fetchone()

                last_pendingindex = PendingIndex.objects.all().order_by('-date_added').first()
                if last_pendingindex:
                    newest_date = last_pendingindex.date_added
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last pending index: {0}'.format(newest_date))
                query = "SELECT * FROM dir_pendingindex WHERE date_added > '{0}' ORDER BY date_added LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer pending indexes:')
                for item in dictfetchall(cursor):
                    print(item)

                last_changelogitem = ChangelogItem.objects.all().order_by('-date_added').first()
                if last_changelogitem:
                    newest_date = last_changelogitem.date_added
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last changelog item: {0}'.format(newest_date))
                query = "SELECT * FROM dir_changelogitem WHERE date_added > '{0}' ORDER BY date_added LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer changelog items:')
                for item in dictfetchall(cursor):
                    print(item)

                last_domainsearchlog = DomainSearchLog.objects.all().order_by('-last_search').first()
                if last_domainsearchlog:
                    newest_date = last_domainsearchlog.last_search
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last domain search log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_domainsearchlog WHERE last_search > '{0}' ORDER BY last_search LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer domain search logs:')
                for item in dictfetchall(cursor):
                    print(item)

                last_ipsearchlog = IPSearchLog.objects.all().order_by('-last_search').first()
                if last_ipsearchlog:
                    newest_date = last_ipsearchlog.last_search
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last IP search log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_ipsearchlog WHERE last_search > '{0}' ORDER BY last_search LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer IP search logs:')
                for item in dictfetchall(cursor):
                    print(item)

                last_indexstats = IndexStats.objects.all().order_by('-create_date').first()
                if last_indexstats:
                    newest_date = last_indexstats.create_date
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last domain search log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_indexstats WHERE create_date > '{0}' ORDER BY create_date LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer index stats:')
                for item in dictfetchall(cursor):
                    print(item)

                last_domainsuffix = DomainSuffix.objects.all().order_by('-last_updated').first()
                if last_domainsuffix:
                    newest_date = last_domainsuffix.last_updated
                    newest_date = '2010-01-01'
                else:
                    newest_date = '2010-01-01'
                print('Last domain suffix: {0}'.format(newest_date))
                query = "SELECT * FROM dir_domainsuffix WHERE last_updated > '{0}' ORDER BY last_updated LIMIT 10".format(newest_date)
                cursor.execute(query)
                print('Newer domain suffixes:')
                for item in dictfetchall(cursor):
                    print(item)
