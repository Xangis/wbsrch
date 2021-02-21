# -*- coding: utf-8 -*-
from django.db import connections
from django.core.management.base import BaseCommand
from dir.models import language_list, ChangelogItem, DomainSearchLog, IPSearchLog, DomainSuffix, IndexStats, DomainInfo, BlockedSite
from dir.utils import GetSearchLogModelFromLanguage, GetPendingIndexModelFromLanguage, GetIndexModelFromLanguage, GetKeywordRankingModelFromLanguage, GetResultClickModelFromLanguage


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
        language_list = [options['language'], ]
        for language in language_list:
            remote_searchlog_model = 'dir_searchlog'
            remote_pendingindex_model = 'dir_pendingindex'
            remote_index_model = 'dir_indexterm'
            remote_keywordranking_model = 'dir_keywordranking'
            remote_resultclick_model = 'dir_resultclick'
            searchlog_model = GetSearchLogModelFromLanguage(language)
            pendingindex_model = GetPendingIndexModelFromLanguage(language)
            index_model = GetIndexModelFromLanguage(language)
            keywordranking_model = GetKeywordRankingModelFromLanguage(language)
            resultclick_model = GetResultClickModelFromLanguage(language)
            if language != 'en':
                remote_searchlog_model = 'dir_searchlog_' + language
                remote_pendingindex_model = 'dir_pendingindex_' + language
                remote_index_model = 'dir_indexterm_' + language
                remote_keywordranking_model = 'dir_keywordranking_' + language
                remote_resultclick_model = 'dir_resultclick_' + language
            with connections['live_indexes'].cursor() as cursor:
                last_log = searchlog_model.objects.all().order_by('-last_search').first()
                if last_log:
                    newest_date = last_log.last_search
                else:
                    newest_date = '2010-01-01'
                print('Last log: {0}'.format(newest_date))
                query = "SELECT * FROM {0} WHERE last_search > %s ORDER BY last_search".format(remote_searchlog_model)
                cursor.execute(query, [newest_date])
                print('Newer search logs:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 5738100, 'keywords': 'belia', 'result_count': 250, 'last_search': datetime.datetime(2016, 5, 1, 19, 24, 50, 936411, tzinfo=<UTC>),
                    # 'search_time': Decimal('0.07'), 'indexed': True, 'referer': None, 'ip': '207.46.13.40',
                    # 'browserstring': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'is_bot': True, 'ip_country': 'US',
                    # 'search_id': UUID('c4b1f620-3691-4d08-9b31-1233af606371')}
                    print(item)
                    sl = searchlog_model()
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
                    searchlog_model.objects.filter(pk=sl.pk).update(last_search=item['last_search'])
                    count += 1
                print('Added {0} new {1} entries.'.format(count, remote_searchlog_model))

                last_pendingindex = pendingindex_model.objects.all().order_by('-date_added').first()
                if last_pendingindex:
                    newest_date = last_pendingindex.date_added
                else:
                    newest_date = '2010-01-01'
                print('Last pending index: {0}'.format(newest_date))
                query = "SELECT * FROM {0} WHERE date_added > %s ORDER BY date_added".format(remote_pendingindex_model)
                cursor.execute(query, [newest_date])
                print('Newer pending indexes:')
                count = 0
                for item in dictfetchall(cursor):
                    # {'id': 11096469, 'keywords': 'youtu.be/xxnyfritezc', 'date_added': datetime.date(2021, 2, 9), 'reason': 'Search youtu.be/xxnyfritezc not indexed yet.'}
                    print(item)
                    keywords = item['keywords']
                    existing = pendingindex_model.objects.filter(keywords=keywords).first()
                    if not existing:
                        pi = pendingindex_model()
                        pi.keywords = keywords
                        pi.date_added = item['date_added']
                        pi.reason = item['reason']
                        pi.save()
                        pendingindex_model.objects.filter(pk=pi.pk).update(date_added=item['date_added'])
                        count += 1
                        print('Added {0} to the database.'.format(remote_pendingindex_model))
                print('Added {0} new {1} entries.'.format(count, remote_pendingindex_model))

                last_changelogitem = ChangelogItem.objects.all().order_by('-date_added').first()
                if last_changelogitem:
                    newest_date = last_changelogitem.date_added
                else:
                    newest_date = '2010-01-01'
                print('Last changelog item: {0}'.format(newest_date))
                query = "SELECT * FROM dir_changelogitem WHERE date_added > %s ORDER BY date_added"
                cursor.execute(query, [newest_date])
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
                query = "SELECT * FROM dir_domainsearchlog WHERE last_search > %s ORDER BY last_search"
                cursor.execute(query, [newest_date])
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
                query = "SELECT * FROM dir_ipsearchlog WHERE last_search > %s ORDER BY last_search"
                cursor.execute(query, [newest_date])
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

                query = "SELECT * FROM dir_blockedsite ORDER BY date_added DESC LIMIT 1"
                cursor.execute(query)
                newest_date = '2010-01-01'
                for item in dictfetchall(cursor):
                    newest_date = item['date_added']
                    print('Last blocked site: {0}'.format(newest_date))
                last_blockedsites = BlockedSite.objects.filter(date_added__gt=newest_date).order_by('date_added')
                print('Newer blocked sites:')
                count = 0
                for item in last_blockedsites:
                    print(item.__dict__)
                    query = "INSERT INTO dir_blockedsite (url, reason, detailedreason, exclude_subdomains, date_added) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(query, [item.url, item.reason, item.detailedreason, item.exclude_subdomains, item.date_added])
                    count += 1
                print('Added {0} new BlockedSite entries'.format(count))

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

                query = "SELECT * FROM dir_domaininfo ORDER BY last_updated DESC LIMIT 1"
                cursor.execute(query)
                newest_date = '2010-01-01'
                for item in dictfetchall(cursor):
                    newest_date = item['last_updated']
                    print('Last updated domain info: {0}'.format(newest_date))
                last_domains = DomainInfo.objects.filter(last_updated__gt=newest_date).order_by('last_updated')
                print('{0} domain infos are newer on the local machine'.format(last_domains.count()))
                count = 0
                updated = 0

                for item in last_domains:
                    cursor.execute("SELECT count(*) FROM dir_domaininfo WHERE url = %s", [item.url])
                    existing_count = cursor.fetchone()[0]
                    if existing_count > 0:
                        print('Updating {0}'.format(item.url))
                        query = ("UPDATE dir_domaininfo SET language_association = %s, notes = %s, rank_adjustment = %s, "
                                 "rank_reason = %s, alexa_rank = %s, alexa_rank_date = %s, alexa_outdated = %s, "
                                 "majestic_rank = %s, majestic_refsubnets = %s, majestic_rank_date = %s, majestic_outdated = %s, "
                                 "quantcast_rank = %s, quantcast_rank_date = %s, quantcast_outdated = %s, domcop_rank = %s, "
                                 "domcop_pagerank = %s, domcop_pagerank_date = %s, domcop_pagerank_outdated = %s, "
                                  "uses_language_subdirs = %s, uses_language_query_parameter = %s, uses_langid = %s, "
                                  "is_unblockable = %s, domain_created = %s, domain_expires = %s, domain_updated = %s, "
                                  "whois_last_updated = %s, robots_ip = %s, robots_txt = %s, robots_last_updated = %s, "
                                  "domains_linking_in = %s, domains_linking_in_last_updated = %s, verified_notporn = %s, "
                                  "num_urls = %s, num_urls_last_updated = %s, num_keywords_ranked = %s, "
                                  "num_keywords_last_updated = %s, favicons_last_updated = %s, whois_name = %s, whois_city = %s, "
                                  "whois_country = %s, whois_state = %s, whois_address = %s, whois_org = %s, whois_registrar = %s, "
                                  "whois_zipcode = %s, whois_nameservers = %s, whois_emails = %s, "
                                  "last_updated = current_timestamp WHERE url = %s")
                        cursor.execute(query, [item.language_association, item.notes, item.rank_adjustment, item.rank_reason,
                            item.alexa_rank, item.alexa_rank_date, item.alexa_outdated, item.majestic_rank, item.majestic_refsubnets,
                            item.majestic_rank_date, item.majestic_outdated, item.quantcast_rank, item.quantcast_rank_date,
                            item.quantcast_outdated, item.domcop_rank, item.domcop_pagerank, item.domcop_pagerank_date,
                            item.domcop_pagerank_outdated, item.uses_language_subdirs, item.uses_language_query_parameter, item.uses_langid,
                            item.is_unblockable, item.domain_created, item.domain_expires, item.domain_updated,
                            item.whois_last_updated, item.robots_ip, item.robots_txt, item.robots_last_updated, item.domains_linking_in,
                            item.domains_linking_in_last_updated, item.verified_notporn, item.num_urls,
                            item.num_urls_last_updated, item.num_keywords_ranked, item.num_keywords_last_updated, item.favicons_last_updated,
                            item.whois_name, item.whois_city, item.whois_country, item.whois_state, item.whois_address, item.whois_org,
                            item.whois_registrar, item.whois_zipcode, item.whois_nameservers, item.whois_emails, item.url])
                        updated += 1
                    else:
                        print('Adding {0}'.format(item.url))
                        query = ("INSERT INTO dir_domaininfo (url, language_association, notes, rank_adjustment, rank_reason, "
                                 "alexa_rank, alexa_rank_date, alexa_outdated, majestic_rank, majestic_refsubnets, majestic_rank_date, "
                                 "majestic_outdated, quantcast_rank, quantcast_rank_date, quantcast_outdated, domcop_rank, "
                                 "domcop_pagerank, domcop_pagerank_date, domcop_pagerank_outdated, uses_language_subdirs, "
                                 "uses_language_query_parameter, uses_langid, is_unblockable, domain_created, domain_expires, "
                                 "domain_updated, whois_last_updated, robots_ip, robots_txt, robots_last_updated, domains_linking_in, "
                                 "domains_linking_in_last_updated, verified_notporn, num_urls, num_urls_last_updated, "
                                 "num_keywords_ranked, num_keywords_last_updated, favicons_last_updated, whois_name, whois_city, "
                                 "whois_country, whois_state, whois_address, whois_org, whois_registrar, whois_zipcode, whois_nameservers, "
                                 "whois_emails, last_updated) VALUES "
                                 "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp)")
                        cursor.execute(query, [item.url, item.language_association, item.notes, item.rank_adjustment,
                            item.rank_reason, item.alexa_rank, item.alexa_rank_date, item.alexa_outdated, item.majestic_rank,
                            item.majestic_refsubnets, item.majestic_rank_date, item.majestic_outdated, item.quantcast_rank,
                            item.quantcast_rank_date, item.quantcast_outdated, item.domcop_rank, item.domcop_pagerank,
                            item.domcop_pagerank_date, item.domcop_pagerank_outdated, item.uses_language_subdirs,
                            item.uses_language_query_parameter, item.uses_langid, item.is_unblockable,
                            item.domain_created, item.domain_expires, item.domain_updated, item.whois_last_updated, item.robots_ip,
                            item.robots_txt, item.robots_last_updated, item.domains_linking_in, item.domains_linking_in_last_updated,
                            item.verified_notporn, item.num_urls, item.num_urls_last_updated,
                            item.num_keywords_ranked, item.num_keywords_last_updated, item.favicons_last_updated,
                            item.whois_name, item.whois_city, item.whois_country, item.whois_state, item.whois_address, item.whois_org,
                            item.whois_registrar, item.whois_zipcode, item.whois_nameservers, item.whois_emails])
                        count += 1
                print('Added {0} new DomainInfo entries and updated {1} existing DomainInfo entries.'.format(count, updated))

                query = "SELECT * FROM {0} ORDER BY date_indexed DESC LIMIT 1".format(remote_index_model)
                cursor.execute(query)
                newest_date = '2010-01-01'
                for item in dictfetchall(cursor):
                    newest_date = item['date_indexed']
                    print('Last index term: {0}'.format(newest_date))
                last_terms = index_model.objects.filter(date_indexed__gt=newest_date).order_by('date_indexed')
                print('{0} index terms are newer on the local machine'.format(last_terms.count()))
                count = 0
                updated = 0
                for item in last_terms:
                    query = "SELECT count(*) FROM {0} WHERE keywords = %s".format(remote_index_model)
                    cursor.execute(query, [item.keywords])
                    existing_count = cursor.fetchone()[0]
                    if existing_count > 0:
                        print('Updating {0}'.format(item.keywords))
                        # show_ad and verified_english only exist in the English-language index
                        if language == 'en':
                            query = ("UPDATE {0} SET page_rankings = %s, num_results = %s, num_pages = %s, "
                                     "index_time = %s, search_results = %s, actively_blocked = %s, refused = %s, "
                                     "typo_for = %s, is_language = %s, term_weight = %s, date_indexed = %s, show_ad = %s, "
                                     "verified_english = %s WHERE keywords = %s").format(remote_index_model)
                            cursor.execute(query, [item.page_rankings, item.num_results, item.num_pages, item.index_time,
                                item.search_results, item.actively_blocked, item.refused, item.typo_for, item.is_language,
                                item.term_weight, item.date_indexed, item.show_ad, item.verified_english, item.keywords])
                        else:
                            query = ("UPDATE {0} SET page_rankings = %s, num_results = %s, num_pages = %s, "
                                     "index_time = %s, search_results = %s, actively_blocked = %s, refused = %s, "
                                     "typo_for = %s, is_language = %s, term_weight = %s, date_indexed = %s "
                                     "WHERE keywords = %s").format(remote_index_model)
                            cursor.execute(query, [item.page_rankings, item.num_results, item.num_pages, item.index_time,
                                item.search_results, item.actively_blocked, item.refused, item.typo_for, item.is_language,
                                item.term_weight, item.date_indexed, item.keywords])
                        updated += 1
                        # Now delete keyword ranking info so we can replace it later.
                        query = 'DELETE FROM {0} WHERE keywords = %s'.format(remote_keywordranking_model)
                        cursor.execute(query, [item.keywords])
                        deleted_count = cursor.rowcount
                        if deleted_count > 0:
                            print('Deleted {0} keyword rankings.'.format(deleted_count))
                    else:
                        print('Adding {0}'.format(item.keywords))
                        query = ("INSERT INTO {0} (keywords, page_rankings, num_results, num_pages, index_time, "
                                 "search_results, actively_blocked, refused, typo_for, is_language, term_weight, "
                                 "date_indexed, show_ad, verified_english) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(remote_index_model)
                        cursor.execute(query, [item.keywords, item.page_rankings, item.num_results, item.num_pages,
                            item.index_time, item.search_results, item.actively_blocked, item.refused, item.typo_for,
                            item.is_language, item.term_weight, item.date_indexed, item.show_ad, item.verified_english])
                        count += 1
                    keywords = keywordranking_model.objects.filter(keywords=item.keywords)
                    query = ("INSERT INTO {0} (keywords, rank, rooturl, show) VALUES (%s, %s, %s, %s)").format(remote_keywordranking_model)
                    num_rankings = 0
                    for keyword in keywords:
                        cursor.execute(query, [keyword.keywords, keyword.rank, keyword.rooturl, keyword.show])
                        num_rankings += 1
                    print('Added {0} keyword rankings'.format(num_rankings))
                print('Added {0} new {2} entries and updated {1} existing {2} entries.'.format(count, updated, remote_index_model))

                last_domainsuffix = DomainSuffix.objects.all().order_by('-last_updated').first()
                if last_domainsuffix:
                    newest_date = last_domainsuffix.last_updated
                else:
                    newest_date = '2010-01-01'
                print('Last domain suffix: {0}'.format(newest_date))
                query = "SELECT * FROM dir_domainsuffix WHERE last_updated > %s ORDER BY last_updated"
                cursor.execute(query, [newest_date])
                print('Newer domain suffixes:')
                for item in dictfetchall(cursor):
                    print(item)

                last_resultclick = resultclick_model.objects.all().order_by('-click_time').first()
                if last_resultclick:
                    newest_date = last_resultclick.click_time
                else:
                    newest_date = '2010-01-01'
                print('Last result click: {0}'.format(newest_date))
                query = "SELECT * FROM {0} WHERE click_time > %s ORDER BY click_time".format(remote_resultclick_model)
                cursor.execute(query, [newest_date])
                print('Newer result clicks:')
                count = 0
                for item in dictfetchall(cursor):
                    print(item)
                    rc = resultclick_model()
                    rc.keywords = item['keywords']
                    rc.search_id = item['search_id']
                    rc.position = item['position']
                    rc.ip = item['ip']
                    rc.url = item['url']
                    rc.click_time = item['click_time']
                    rc.xpos = item['xpos']
                    rc.ypos = item['ypos']
                    rc.save()
                    resultclick_model.objects.filter(pk=rc.pk).update(click_time=item['click_time'])
                    count += 1
                print('Added {0} new {1} entries.'.format(count, remote_resultclick_model))
