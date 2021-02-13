# -*- coding: utf-8 -*-
from django.db import connections
from django.core.management.base import BaseCommand
from dir.models import SearchLog, PendingIndex, language_list, ChangelogItem, DomainSearchLog, IPSearchLog, DomainSuffix, IndexStats, ResultClick


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

    def handle(self, *args, **options):
        for language in language_list:
            if language != 'en':
                # TODO: implement other languages.
                continue
            with connections['live_indexes'].cursor() as cursor:
                last_log = SearchLog.objects.all().order_by('-last_search').first()
                if last_log:
                    newest_date = last_log.last_search
                else:
                    newest_date = '2010-01-01'
                print('Last log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_searchlog WHERE last_search > '{0}' ORDER BY last_search".format(newest_date)
                cursor.execute(query)
                print('Newer search logs:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 5738100, 'keywords': 'belia', 'result_count': 250, 'last_search': datetime.datetime(2016, 5, 1, 19, 24, 50, 936411, tzinfo=<UTC>),
                    # 'search_time': Decimal('0.07'), 'indexed': True, 'referer': None, 'ip': '207.46.13.40',
                    # 'browserstring': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'is_bot': True, 'ip_country': 'US',
                    # 'search_id': UUID('c4b1f620-3691-4d08-9b31-1233af606371')}
                    print(item)
                    sl = SearchLog()
                    sl.keywords = item['keywords']
                    sl.result_count = item['result_count']
                    sl.last_search = item['last_search']
                    sl.search_time = item['search_time']
                    sl.indexed = item['indexed']
                    sl.referer = item['referer']
                    sl.ip = item['ip']
                    sl.ip_country = item['ip_country']
                    sl.browserstring = item['browserstring']
                    sl.is_bot = item['is_bot']
                    sl.search_id = item['search_id']
                    sl.save()
                    SearchLog.objects.filter(pk=sl.pk).update(last_search=item['last_search'])
                    count += 1
                print('Added {0} new SearchLog entries'.format(count))

                last_pendingindex = PendingIndex.objects.all().order_by('-date_added').first()
                if last_pendingindex:
                    newest_date = last_pendingindex.date_added
                else:
                    newest_date = '2010-01-01'
                print('Last pending index: {0}'.format(newest_date))
                query = "SELECT * FROM dir_pendingindex WHERE date_added > '{0}' ORDER BY date_added".format(newest_date)
                cursor.execute(query)
                print('Newer pending indexes:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 11096469, 'keywords': 'youtu.be/xxnyfritezc', 'date_added': datetime.date(2021, 2, 9), 'reason': 'Search youtu.be/xxnyfritezc not indexed yet.'}
                    print(item)
                    keywords = item['keywords']
                    existing = PendingIndex.objects.filter(keywords=keywords).first()
                    if not existing:
                        pi = PendingIndex()
                        pi.keywords = keywords
                        pi.date_added = item['date_added']
                        pi.reason = item['reason']
                        pi.save()
                        PendingIndex.objects.filter(pk=pi.pk).update(date_added=item['date_added'])
                        count += 1
                        print('Added PendingIndex to the database.')
                print('Added {0} new PendingIndex entries.'.format(count))

                last_changelogitem = ChangelogItem.objects.all().order_by('-date_added').first()
                if last_changelogitem:
                    newest_date = last_changelogitem.date_added
                else:
                    newest_date = '2010-01-01'
                print('Last changelog item: {0}'.format(newest_date))
                query = "SELECT * FROM dir_changelogitem WHERE date_added > '{0}' ORDER BY date_added".format(newest_date)
                cursor.execute(query)
                print('Newer changelog items:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 189, 'title': None, 'num_urls_crawled': 24920000, 'num_terms_indexed': 3090000,
                    # 'num_domains_blocked': 970000, 'comment': 'After a hiatus, we are back with a different approach to managing our data.',
                    # 'date_added': datetime.date(2020, 12, 26), 'version': '1.04'}
                    print(item)
                    cl = ChangelogItem()
                    cl.title = item['title']
                    cl.num_urls_crawled = item['num_urls_crawled']
                    cl.num_terms_indexed = item['num_terms_indexed']
                    cl.num_domains_blocked = item['num_domains_blocked']
                    cl.comment = item['comment']
                    cl.date_added = item['date_added']
                    cl.version = item['version']
                    cl.save()
                    count += 1
                    print('Added ChangelogItem to the database.')
                print('Added {0} new ChangelogItem entries.'.format(count))

                last_domainsearchlog = DomainSearchLog.objects.all().order_by('-last_search').first()
                if last_domainsearchlog:
                    newest_date = last_domainsearchlog.last_search
                else:
                    newest_date = '2010-01-01'
                print('Last domain search log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_domainsearchlog WHERE last_search > '{0}' ORDER BY last_search".format(newest_date)
                cursor.execute(query)
                print('Newer domain search logs:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 16104487, 'keywords': 'www.loot.co.za', 'result_count': 1,
                    # 'last_search': datetime.datetime(2021, 2, 12, 22, 30, 14, 98251, tzinfo=<UTC>),
                    # 'search_time': Decimal('0.09'), 'indexed': False, 'referer': None, 'ip': '',
                    # 'browserstring': 'Mozilla/5.0 (compatible; BLEXBot/1.0; +http://webmeup-crawler.com/)',
                    # 'is_bot': True, 'language': 'en', 'ip_country': None, 'search_id': UUID('a6e018b3-cf41-41ed-9bd9-33a4f76fea45')}
                    print(item)
                    dl = DomainSearchLog()
                    dl.keywords = item['keywords']
                    dl.result_count = item['result_count']
                    dl.last_search = item['last_search']
                    dl.search_time = item['search_time']
                    dl.indexed = item['indexed']
                    dl.referer = item['referer']
                    dl.ip = item['ip']
                    dl.ip_country = item['ip_country']
                    dl.browserstring = item['browserstring']
                    dl.is_bot = item['is_bot']
                    dl.language = item['language']
                    dl.search_id = item['search_id']
                    dl.save()
                    DomainSearchLog.objects.filter(pk=dl.pk).update(last_search=item['last_search'])
                    count += 1
                print('Added {0} new DomainSearchLog entries'.format(count))

                last_ipsearchlog = IPSearchLog.objects.all().order_by('-last_search').first()
                if last_ipsearchlog:
                    newest_date = last_ipsearchlog.last_search
                else:
                    newest_date = '2010-01-01'
                print('Last IP search log: {0}'.format(newest_date))
                query = "SELECT * FROM dir_ipsearchlog WHERE last_search > '{0}' ORDER BY last_search".format(newest_date)
                cursor.execute(query)
                print('Newer IP search logs:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 246374, 'keywords': '216.127.60.12', 'result_count': 31,
                    # 'last_search': datetime.datetime(2021, 2, 12, 22, 36, 42, 250266, tzinfo=<UTC>),
                    # 'search_time': Decimal('0.06'), 'indexed': False, 'referer': None, 'ip': '', 'ip_country': None,
                    # 'browserstring': 'Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)',
                    # 'is_bot': True, 'language': 'en', 'search_id': UUID('f5ffd777-80f5-4e74-b874-6c23f11a2db8')}
                    print(item)
                    il = IPSearchLog()
                    il.keywords = item['keywords']
                    il.result_count = item['result_count']
                    il.last_search = item['last_search']
                    il.search_time = item['search_time']
                    il.indexed = item['indexed']
                    il.referer = item['referer']
                    il.ip = item['ip']
                    il.ip_country = item['ip_country']
                    il.browserstring = item['browserstring']
                    il.is_bot = item['is_bot']
                    il.language = item['language']
                    il.search_id = item['search_id']
                    il.save()
                    IPSearchLog.objects.filter(pk=il.pk).update(last_search=item['last_search'])
                    count += 1
                print('Added {0} new IPSearchLog entries'.format(count))

                query = "SELECT * FROM dir_indexstats ORDER BY create_date DESC LIMIT 1"
                cursor.execute(query)
                newest_date = '2010-01-01'
                for item in dictfetchall(cursor):
                    newest_date = item['create_date']
                    print('Last index stats: {0}'.format(newest_date))
                last_indexstats = IndexStats.objects.filter(create_date__gt=newest_date).order_by('create_date')
                print('Newer index stats:')
                count = 0
                for item in last_indexstats:
                    print(item.__dict__)
                    query = "INSERT INTO dir_indexstats (num_excluded, langs, total_urls, total_indexes, total_pendingindexes, create_date, most_linked_to_domains, last_most_linked_to, generation_time) VALUES ({0}, '{1}', {2}, {3}, {4}, '{5}', '{6}', '{7}', {8})".format(
                        item.num_excluded, item.langs, item.total_urls, item.total_indexes, item.total_pendingindexes, item.create_date, item.most_linked_to_domains, item.last_most_linked_to, item.generation_time)
                    print(query)
                    cursor.execute(query)
                    count += 1
                print('Added {0} new IndexStats entries'.format(count))

                last_domainsuffix = DomainSuffix.objects.all().order_by('-last_updated').first()
                if last_domainsuffix:
                    newest_date = last_domainsuffix.last_updated
                else:
                    newest_date = '2010-01-01'
                print('Last domain suffix: {0}'.format(newest_date))
                query = "SELECT * FROM dir_domainsuffix WHERE last_updated > '{0}' ORDER BY last_updated".format(newest_date)
                cursor.execute(query)
                print('Newer domain suffixes:')
                for item in dictfetchall(cursor):
                    print(item)

                last_resultclick = ResultClick.objects.all().order_by('-click_time').first()
                if last_resultclick:
                    newest_date = last_resultclick.click_time
                else:
                    newest_date = '2010-01-01'
                print('Last result click: {0}'.format(newest_date))
                query = "SELECT * FROM dir_resultclick WHERE click_time > '{0}' ORDER BY click_time".format(newest_date)
                cursor.execute(query)
                print('Newer result clicks:')
                count = 0
                for item in dictfetchall(cursor):
                    print(item)
                    rc = ResultClick()
                    rc.keywords = item['keywords']
                    rc.search_id = item['search_id']
                    rc.position = item['position']
                    rc.ip = item['ip']
                    rc.url = item['url']
                    rc.click_time = item['click_time']
                    rc.xpos = item['xpos']
                    rc.ypos = item['ypos']
                    rc.save()
                    ResultClick.objects.filter(pk=rc.pk).update(click_time=item['click_time'])
                    count += 1
                print('Added {0} new ResultClick entries.'.format(count))
