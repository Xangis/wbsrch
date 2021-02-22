# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.core.cache import cache
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import ujson
import json  # Needed for autocomplete encoding handling.
from dir.models import *
from dir.utils import *
from django_q.tasks import async_task
from dir.language import language_name_reverse
from dir.crawler import CrawlSingleUrl, Crawler
from urllib.parse import urlparse
from datetime import date, timedelta
import itertools
import uuid
from django.contrib.gis.geoip import GeoIP
from django.core.mail import send_mail

INDEX_TERM_STALE_DAYS = 1460
MAX_SEARCH_RESULTS = 100


def SaveLogEntry(log):
    """
    Save a search log entry, be it a domain search or regular search. Intended to
    be called asynchronously to avoid making users wait for a search log to commit
    before getting results.
    """
    log.save()


def LanguageFromDomain(request):
    prefix = None
    try:
        prefix = request.META['HTTP_HOST'].split('.')[0]
        if prefix == 'no':
            prefix = 'nb'
    except KeyError:
        pass
    if not prefix or prefix not in language_list:
        return 'en'
    return prefix


class SearchResult():
    def __init__(self, language):
        self.allfromdomain = False
        self.result_count = 0
        self.searchterm = None
        self.indexed = True
        self.actively_blocked = False
        self.search_results = []
        self.language_code = language
        self.show_sd_ad = False
        self.show_network_ad = True  # Fallback if we shouldn't show the SD ad.
        self.typo_for = None
        self.typo = None
        self.is_language = None
        self.names_language = None
        self.names_language_search = None
        self.refused = False
        self.is_domain = None
        self.is_ip = None
        self.date_indexed = None
        if self.language_code == 'en-us':
            self.language_code = 'en'


# Takes a search result class, which may or may not be empty, and merges it with an
# index term's search data.
def MergeSearchResult(search_result, index_term, bonus_existing=False):
    if index_term.actively_blocked:
        search_result.actively_blocked = True
        search_result.show_network_ad = False
    if index_term.refused:
        search_result.show_network_ad = False
        search_result.show_sd_ad = False
        search_result.refused = True
    if index_term.typo_for:
        search_result.typo_for = index_term.typo_for
        search_result.typo = index_term.keywords
    if index_term.is_language:
        search_result.is_language = index_term.is_language
    try:
        if index_term.show_sd_ad:
            search_result.show_sd_ad = True
    except Exception:
        pass

    # Set the index date. Add dates to string for multiple terms.
    if not search_result.date_indexed:
        search_result.date_indexed = '{0}'.format(index_term.date_indexed)
    else:
        search_result.date_indexed = '{0}, {1}'.format(search_result.date_indexed, index_term.date_indexed)
    if not index_term.search_results:
        tmp_result = []
    else:
        tmp_result = ujson.loads(index_term.search_results)
    if search_result.allfromdomain:
        found = False
        for result in tmp_result:
            if result[0] == search_result.allfromdomain:
                tmp_result = [result, ]
                found = True
                break
            alternateurl = result[1].get('alternateurl', None)
            if alternateurl and alternateurl == search_result.allfromdomain:
                tmp_result = [result, ]
                found = True
                break
        if not found:
            tmp_result = []

    if not search_result.allfromdomain:
        search_result.result_count += len(tmp_result)
    else:
        if len(tmp_result) > 0:
            result_list = tmp_result[0]
            search_result.result_count += len(result_list[1]['urls'])

    if search_result.search_results == []:
        search_result.search_results = tmp_result
        return search_result

    new_result = []
    for idx, item in enumerate(itertools.chain(search_result.search_results, tmp_result)):
        if not any(item[0] in url for url in new_result):
            new_result.append(item)
        else:
            for iteridx, iteritem in enumerate(new_result):
                if iteritem[0] == item[0]:
                    # bonus_existing means we give a bonus to results that appear in both.
                    # it's used for combining terms that aren't indexed yet.
                    if bonus_existing:
                        new_result[iteridx][1]['score'] = (new_result[iteridx][1]['score'] + item[1]['score']) * 2
                    else:
                        new_result[iteridx][1]['score'] = new_result[iteridx][1]['score'] + item[1]['score']
                    new_result[iteridx][1]['urls'].append(item[1]['urls'])
                    # TODO: Sort the appended urls for that domain.
                    # This line complains about list indexes needing to be integers, not strings.
                    # new_result[iteridx][1]['urls'].sort(key=itemgetter('score'), reverse=True)
    new_result.sort(key=lambda item: item[1]['score'], reverse=True)
    search_result.search_results = new_result
    return search_result


def RemoveWordFromSearchResults(search_result, word):
    """
    Removes any results from a search that have the specified word in their
    title or description.
    """
    tmp_results = []
    for idx, result in search_result.search_results:
        tmp_urls = []
        for page in result['urls']:
            try:
                resultitems = page['description'].lower().split(' ')
            except AttributeError:
                resultitems = []
            titleitems = page['title'].lower().split(' ')
            # TODO: Remove page-by-page instead of skipping entire result if one page matches.
            if word in resultitems or word in titleitems:
                print('Word {0} found in page {1}, removing.'.format(word, page['url']))
            else:
                tmp_urls.append(page)
        if len(tmp_urls) > 0:
            result['urls'] = tmp_urls
            tmp_results.append([id, result])
        # NEED TO REPLACE THE ITEMS AND THE CURENT INDEX POINTER.
    search_result.search_results = tmp_results
    search_result.result_count = len(search_result.search_results)
    return search_result


def index(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    superuser = False
    if request.user and request.user.is_superuser:
        superuser = True

    cached = False

    return render(request, 'index.htm', {'language_code': language_code, 'superuser': superuser, 'cached': cached})


def ads(request):
    return HttpResponsePermanentRedirect('https://ads.wbsrch.com')


def analytics(request):
    return HttpResponsePermanentRedirect('https://analytics.wbsrch.com')


def apps(request):
    return HttpResponsePermanentRedirect('https://apps.wbsrch.com')


def images(request):
    return HttpResponsePermanentRedirect('https://images.wbsrch.com')


def maps(request):
    return HttpResponsePermanentRedirect('https://maps.wbsrch.com')


def news(request):
    return HttpResponsePermanentRedirect('https://news.wbsrch.com')


def stats(request):
    return HttpResponsePermanentRedirect('https://stats.wbsrch.com')


def video(request):
    return HttpResponsePermanentRedirect('https://video.wbsrch.com')


def policy(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('policy.htm', {'language_code': language_code})


def philosophy(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('philosophy.htm', {'language_code': language_code})


def faq(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('faq.htm', {'language_code': language_code})


def dmca(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('dmca.htm', {'language_code': language_code})


def dmca_notices(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    notices = DMCANotice.objects.all()
    return render_to_response('dmcanotices.htm', {'language_code': language_code, 'notices': notices})


def howto(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('howto.htm', {'language_code': language_code})


def privacy(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('privacy.htm', {'language_code': language_code})


def criteria(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('criteria.htm', {'language_code': language_code})


def wbrank(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('wbrank.htm', {'language_code': language_code})


def changelog(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    cached = False
    changelog = cache.get('changelog')
    if not changelog:
        changelog = list(ChangelogItem.objects.filter(date_added__lte=timezone.now()).order_by('-date_added'))
        # Cache for up to 1 hour.
        cache.set('changelog', changelog, 3600)
    else:
        cached = True
    return render_to_response('changelog.htm', {'changelog': changelog, 'language_code': language_code, 'cached': cached})


def terms(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('terms.htm', {'language_code': language_code})


def contact(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('contact.htm', {'language_code': language_code})


def hardware(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    return render_to_response('hardware.htm', {'language_code': language_code})


def index_stats(request, realtime=False):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    if realtime:
        stats = GenerateIndexStats(False)
        stats.langs = ujson.loads(stats.langs)
    else:
        try:
            stats = IndexStats.objects.all()[0]
        except Exception:
            # Will only happen with an empty database.
            stats = GenerateIndexStats(True)
        stats.langs = ujson.loads(stats.langs)
    return render_to_response('indexstats.htm', {'language_code': language_code, 'stats': stats})


def tld_stats(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    stats = DomainSuffix.objects.all()
    count = stats.count()
    return render_to_response('tldstats.htm', {'language_code': language_code, 'stats': stats, 'count': count})


def domain(request):
    start = timezone.now()
    if request.method != 'GET':
        raise Http404
    language_code = request.LANGUAGE_CODE
    superuser = False
    cached = False
    notdomain = False
    if request.user and request.user.is_superuser:
        superuser = True
    domain = request.GET.get('q', None)
    if domain:
        domain = domain.lower().strip()
    if domain:
        if BannedSearchString(domain):
            return HttpResponseForbidden('Only a bot would make this request. Denied.')
        rawdomain = domain
        # site_model = GetSiteInfoModelFromLanguage(language_code)
        ranking_model = GetKeywordRankingModelFromLanguage(language_code)
        # Normalize URL
        if domain.startswith('http:') or domain.startswith('https:'):
            parsedurl = urlparse(domain)
            domain = parsedurl.geturl()
            rawdomain = parsedurl.netloc
        if '/' in rawdomain:
            pieces = rawdomain.split('/')
            rawdomain = pieces[0]
        if '.' not in domain or ' ' in domain:
            notdomain = True
        # Prevent crawling excluded sites.
        domains = DomainInfo.objects.filter(url=rawdomain)
        excluded = BlockedSite.objects.filter(url=rawdomain)
        blocked = False
        if excluded.count() > 0:
            blocked = True
        extra = None
        parent = None
        pieces = rawdomain.split('.')
        if not rawdomain.startswith('www.'):
            if len(pieces) > 2:
                parentdomain = '.'.join(pieces[1:])
                try:
                    parent = DomainInfo.objects.get(url=parentdomain)
                except ObjectDoesNotExist:
                    pass
            try:
                extra = DomainInfo.objects.get(url=('www.' + rawdomain))
            except ObjectDoesNotExist:
                pass
        else:
            if len(pieces) > 3:
                parentdomain = '.'.join(pieces[2:])
                try:
                    parent = DomainInfo.objects.get(url=parentdomain)
                except ObjectDoesNotExist:
                    pass
            try:
                extra = DomainInfo.objects.get(url=(rawdomain[4:]))
            except ObjectDoesNotExist:
                pass

        # Get pages for site, but only if it's not blocked.
        # siteinfos = []
        #if not blocked:
        #    siteinfos = site_model.objects.filter(rooturl=rawdomain).values('id', 'url', 'pagetitle', 'pagedescription', 'pagetext', 'rooturl')[:MAX_SEARCH_RESULTS]

        #num_records = len(siteinfos)
        #if num_records >= 200:
        #    num_records = "at least 200"

        # Get cached keyword rankings if available, otherwise query and cache.
        # But only do this if the domain is not blocked.
        rankings = []
        if not blocked:
            rankings = cache.get('rankings_' + language_code + '_' + rawdomain)
            if not rankings:
                rankings = list(ranking_model.objects.filter(rooturl=rawdomain, rank__lte=MAX_SEARCH_RESULTS, show=True).order_by('rank', 'keywords')[0:100])
            # Cache for up to 3 days (in seconds).
                cache.set('rankings_' + language_code + '_' + rawdomain, rankings, 259200)
            else:
                cached = True

        searchlog = DomainSearchLog()
        searchlog.search_id = uuid.uuid4()
        searchlog.keywords = domain
        searchlog.result_count = domains.count()
        # Enforce domain info if it doesn't exist and we have pages.
        #if searchlog.result_count < 1 and (len(rankings) > 0 or len(siteinfos) > 0):
        #    dominfo = DomainInfo()
        #    dominfo.url = rawdomain
        #    try:
        #        dominfo.save()
        #        domains = [dominfo, ]
        #    except IntegrityError:
        # The only reason we would get an integrity error is if we
        # violate the unique key constraint of the database. If we
        # did that, it means that the term is already in there and we
        # should be able to query it. This can happen when someone
        # searches an unindexed term and re-searches it before the
        # placeholder term finishes creating (which could take a while).
        #        connection._rollback()
        #        try:
        #            dominfo = DomainInfo.objects.get(url=rawdomain)
        #            domains = [dominfo, ]
        #        except ObjectDoesNotExist:
        #            domains = []
        searchlog.indexed = False
        if 'HTTP_REFERER' in request.META:
            searchlog.referer = request.META['HTTP_REFERER']
            if len(searchlog.referer) > 255:
                searchlog.referer = searchlog.referer[0:252] + '...'
        if 'REMOTE_ADDR' in request.META:
            searchlog.ip = request.META['REMOTE_ADDR']
        if 'HTTP_USER_AGENT' in request.META:
            searchlog.browserstring = request.META['HTTP_USER_AGENT']
            if len(searchlog.browserstring) > 255:
                searchlog.browserstring = searchlog.browserstring[0:252] + '...'
            if IsBotAgent(searchlog.browserstring):
                searchlog.is_bot = True
        searchlog.language = language_code
        end_delta = timezone.now() - start
        searchlog.search_time = end_delta.total_seconds()
        if searchlog.ip:
            gi = GeoIP()
            country = gi.country_code(searchlog.ip)
            if country:
                searchlog.ip_country = country
        try:
            async_task(SaveLogEntry, searchlog)
        except Exception:
            print('Cannot save log entry. Redis server may not be running.')

        return render(request, 'domain.htm', {'domains': domains, 'excluded': excluded,
            # 'siteinfos': siteinfos,
            'domain': domain,
            # 'num_records': num_records,
            'language_code': language_code, 'rankings': rankings, 'superuser': superuser, 'extra': extra,
            'excluded': excluded, 'parent': parent, 'cached': cached, 'rawdomain': rawdomain, 'notdomain': notdomain}
            )
    return render(request, 'domain.htm', {'language_code': language_code})


def ipaddry(request):
    start = timezone.now()
    cached = False
    if request.method != 'GET':
        raise Http404
    language_code = request.LANGUAGE_CODE
    superuser = False
    if request.user and request.user.is_superuser:
        superuser = True
    # try:
    if True:
        ip = request.GET.get('q', None)
        if not ip:
            return render(request, 'ip.htm', {'language_code': language_code, 'superuser': superuser})
        pieces = ip.split('.')
        if len(pieces) != 4:
            raise Http404
        try:
            for p in pieces:
                ival = int(p)
                if ival < 0 or ival > 255:
                    raise Http404
        except ValueError:
            raise Http404
        #site_model = GetSiteInfoModelFromLanguage(language_code)
        domains = DomainInfo.objects.filter(robots_ip=ip).values('url', 'language_association')
        siteinfos = None

        # TODO: Calculate this with IP address info.
        #num_siteinfos_cache = cache.get('pages_at_ip_' + ip)
        #if not num_siteinfos_cache:
        #    num_siteinfos = site_model.objects.filter(ip=ip).count()
        # Cache for up to 1 week
        #    cache.set('pages_at_ip_' + ip, num_siteinfos, 604800)
        #else:
        #    cached = True
        #    num_siteinfos = int(num_siteinfos_cache)

        searchlog = IPSearchLog()
        searchlog.search_id = uuid.uuid4()
        searchlog.keywords = ip
        searchlog.result_count = len(domains)
        searchlog.indexed = False
        if 'HTTP_REFERER' in request.META:
            searchlog.referer = request.META['HTTP_REFERER']
            if len(searchlog.referer) > 255:
                searchlog.referer = searchlog.referer[0:252] + '...'
        if 'REMOTE_ADDR' in request.META:
            searchlog.ip = request.META['REMOTE_ADDR']
        if 'HTTP_USER_AGENT' in request.META:
            searchlog.browserstring = request.META['HTTP_USER_AGENT']
            if len(searchlog.browserstring) > 255:
                searchlog.browserstring = searchlog.browserstring[0:252] + '...'
            if IsBotAgent(searchlog.browserstring):
                searchlog.is_bot = True
        searchlog.language = language_code
        end_delta = timezone.now() - start
        searchlog.search_time = end_delta.total_seconds()
        if searchlog.ip:
            gi = GeoIP()
            country = gi.country_code(searchlog.ip)
            if country:
                searchlog.ip_country = country
        try:
            async_task(SaveLogEntry, searchlog)
        except Exception:
            print('Cannot save log entry. Redis server may not be running.')

        return render(request, 'ip.htm', {'domains': domains, 'siteinfos': siteinfos, 'ip': ip, 'language_code': language_code, 'superuser': superuser,
                #'num_siteinfos': num_siteinfos,
                'cached': cached})
    # except:
    #    pass
    return render(request, 'ip.htm', {'language_code': language_code, 'cached': cached})


def search(request):
    log = None
    exclude = []
    start = timezone.now()
    result = SearchResult(request.LANGUAGE_CODE)
    # Handle language
    term_model = GetIndexModelFromLanguage(request.LANGUAGE_CODE)
    searchlog_model = GetSearchLogModelFromLanguage(request.LANGUAGE_CODE)
    # Handle search term.
    multiword = False
    if request.method == 'POST':
        result.searchterm = request.POST.get('q', None)
        result.allfromdomain = request.POST.get('domain', False)
        if request.POST.get('s') == 'fp':
            return HttpResponsePermanentRedirect('/search/?q={0}'.format(result.searchterm))
    elif request.method == 'GET':
        result.searchterm = request.GET.get('q', None)
        result.allfromdomain = request.GET.get('domain', False)
        if request.GET.get('s') == 'fp':
            return HttpResponsePermanentRedirect('/search/?q={0}'.format(result.searchterm))
    # Search
    if result.searchterm:
        result.searchterm = CleanSearchText(result.searchterm)
        if BannedSearchString(result.searchterm):
            return HttpResponseForbidden('Only a bot would make this request. Denied.')
        # Break term into individual words
        pieces = result.searchterm.split(' ')
        if len(pieces) > 1:
            multiword = True
        # Check for named language
        for piece in pieces:
            if piece.startswith('-'):
                if len(piece) > 2 and not piece[1].isdigit() and piece[1] != '-':
                    exclude.append(piece[1:].lower())
                    # This could create a problem in that the /printed/ searchterm will not match.
                    # We solve this by passing exclude to the template and using that to display
                    # the query string in addition to result.searchterm. Removed terms will always
                    # appear at the end.
                    result.searchterm = result.searchterm.replace(piece, '')
                    result.searchterm = result.searchterm.replace('  ', ' ')
                    if result.searchterm.endswith(' '):
                        result.searchterm = result.searchterm[0:-1]
            if piece in language_name_reverse and (language_name_reverse[piece] != request.LANGUAGE_CODE):
                result.names_language = language_name_reverse[piece]
                result.names_language_search = result.searchterm.replace(piece, '')
                # Collapse extra spaces if necessary.
                result.names_language_search = result.names_language_search.replace('  ', ' ')
                result.names_language_search = result.names_language_search.strip()
                break
        if 'site:' in result.searchterm:
            dom = None
            queries = []
            for piece in pieces:
                if piece.startswith('site:'):
                    dom = piece[5:]
                else:
                    queries.append(piece)
            if dom and len(queries) > 0:
                return HttpResponseRedirect('/search/?q={0}&domain={1}'.format(' '.join(queries), dom))
            elif dom and len(queries) == 0:
                return HttpResponseRedirect('/domain/?q={0}'.format(dom))
        # Check whether it's a domain search.
        if '.' in result.searchterm:
            for piece in pieces:
                if '.' in piece:
                    domain_url = GetRootUrl(piece)
                    if IsIPAddress(piece):
                        result.is_ip = piece
                    try:
                        searched_domain = DomainInfo.objects.get(url=domain_url)
                        result.is_domain = searched_domain.url
                    except ObjectDoesNotExist:
                        pass
        # Check whether it's a question. Convert a question to a normal search for now.
        # in the future we may want to infer intent in some way, so that "where is afghanistan?" gets results related to "afghanistan" with "location".
        #
        # This is currently not yet enabled because redirecting a user's searches to another term without any indication that we've done so is
        # problematic.
        #
        # We should probably track both "actual search" and "result query".
        #
        # We should also allow exact matches because "Why Is The Sky Blue?" or "Why Is There Air?" could be an exact movie/album title.
        # question = False
        # if result.searchterm.startswith('what is a '):
        #    result.searchterm = result.searchterm[10:]
        #    question = True
        # elif result.searchterm.startswith('what is the '):
        #    result.searchterm = result.searchterm[12:]
        #    question = True
        # elif result.searchterm.startswith('what is '):
        #    result.searchterm = result.searchterm[8:]
        #    question = True
        # elif result.searchterm.startswith('what are '):
        #    result.searchterm = result.searchterm[9:]
        #    question = True
        # elif result.searchterm.startswith('who is '):
        #    result.searchterm = result.searchterm[8:]
        #    question = True
        # elif result.searchterm.startswith('who is the '):
        #    result.searchterm = result.searchterm[12:]
        #    question = True
        # elif result.searchterm.startswith('where is the '):
        #    result.searchterm = result.searchterm[13:]
        #    question = True
        # elif result.searchterm.startswith('where is '):
        #    result.searchterm = result.searchterm[9:]
        #    question = True
        # elif result.searchterm.startswith('when is '):
        #    result.searchterm = result.searchterm[8:]
        #    question = True
        # elif result.searchterm.startswith('why is the '):
        #    result.searchterm = result.searchterm[11:]
        #    question = True
        # elif result.searchterm.startswith('why is '):
        #    result.searchterm = result.searchterm[7:]
        #    question = True
        # elif result.searchterm.startswith('how is the '):
        #    result.searchterm = result.searchterm[11:]
        #    question = True
        # elif result.searchterm.startswith('how is a '):
        #    result.searchterm = result.searchterm[9:]
        #    question = True
        # elif result.searchterm.startswith('how is '):
        #    result.searchterm = result.searchterm[7:]
        #    question = True
        # if question and result.searchterm.endswith('?'):
        #    result.searchterm = result.searchterm[:-1]
        # Retrieve the data.
        term = TrySearchTerm(result.searchterm, result.language_code)
        if term:
            if term.date_indexed < (timezone.now() - timedelta(days=INDEX_TERM_STALE_DAYS)) and not term.actively_blocked and not term.refused and (len(term.keywords) > 2):
                AddPendingTerm(term.keywords, result.language_code, 'Searched for term older than {0} days'.format(INDEX_TERM_STALE_DAYS))
            result = MergeSearchResult(result, term)
        else:
            create_placeholders = False
            try:
                setting = Setting.objects.get(key='create_placeholders')
                if setting.value == 'True' or setting.value == '1' or setting.value == 'T' or setting.value == 'Y' or setting.value == 'yes' or setting.value == 'true':
                    create_placeholders = True
            except Exception:
                print('Not creating placeholder index term -- create_placeholders setting is false')
            result.indexed = False
            searchterms = GetTerms(result.searchterm)
            for item in searchterms:
                try:
                    term = term_model.objects.get(keywords=item)
                    if term.date_indexed < (timezone.now() - timedelta(days=INDEX_TERM_STALE_DAYS)) and not term.actively_blocked and not term.refused and (len(term.keywords) > 2):
                        AddPendingTerm(term.keywords, result.language_code, 'Searched for term older than {0} days'.format(INDEX_TERM_STALE_DAYS))
                    result = MergeSearchResult(result, term, bonus_existing=True)
                except ObjectDoesNotExist:
                    if create_placeholders:
                        term = CreatePlaceholderIndexTerm(item, result.language_code)
                        result = MergeSearchResult(result, term, bonus_existing=True)
            if multiword:
                if create_placeholders:
                    term = CreatePlaceholderIndexTerm(result.searchterm, result.language_code)
                    result = MergeSearchResult(result, term, bonus_existing=True)
        end_delta = timezone.now() - start
        if len(exclude) > 0:
            for excluded in exclude:
                result = RemoveWordFromSearchResults(result, excluded)
        # Log the search, but only if it didn't come from the front page of a search engine.
        if result.allfromdomain:
            pass
        else:
            log = searchlog_model()
            log.search_id = uuid.uuid4()
            # Prevent 'value too long' errors.
            if len(result.searchterm) > 255:
                log.keywords = result.searchterm[0:252] + '...'
            else:
                log.keywords = result.searchterm
            log.result_count = result.result_count
            log.indexed = result.indexed
            log.search_time = end_delta.total_seconds()
            if 'HTTP_REFERER' in request.META:
                log.referer = request.META['HTTP_REFERER']
                if len(log.referer) > 255:
                    log.referer = log.referer[0:252] + '...'
            if 'REMOTE_ADDR' in request.META:
                log.ip = request.META['REMOTE_ADDR']
            if log.ip:
                gi = GeoIP()
                country = gi.country_code(log.ip)
                if country:
                    log.ip_country = country
            if 'HTTP_USER_AGENT' in request.META:
                log.browserstring = request.META['HTTP_USER_AGENT']
                if len(log.browserstring) > 255:
                    log.browserstring = log.browserstring[0:252] + '...'
                if IsBotAgent(log.browserstring):
                    log.is_bot = True
            try:
                async_task(SaveLogEntry, log)
            except Exception:
                print('Cannot save log entry. Redis server may not be running.')
    is_language_name = None
    if result.is_language:
        try:
            is_language_name = language_names[result.is_language]
        except KeyError:
            # This can happen if the language is "Russian" and that is not on the supported language name list.
            # In this case, we set the language to None and don't worry about it -- it won't try to link to the
            # nonexistant language, but that will still be set on the record for the purpose of tagging and
            # filtering elsewhere.
            is_language_name = None
            result.is_language = None
    names_language_name = None
    if result.names_language:
        names_language_name = language_names[result.names_language]
    superuser = False
    if request.user and request.user.is_superuser:
        superuser = True
    if result.refused:
        result.search_results = None
        result.result_count = 0
    if result.result_count > MAX_SEARCH_RESULTS:
        result.search_results = result.search_results[0:MAX_SEARCH_RESULTS]
        result.result_count = MAX_SEARCH_RESULTS
    # Replace typo word in search term so we can correct multi-word phrases. We cannot, however,
    # correct multiple typos in a phrase.
    if result.typo_for:
        result.typo_for = result.searchterm.replace(result.typo, result.typo_for)
    return render(request, 'search.htm',
        {'search_results': result.search_results, 'searchterm': result.searchterm,
          'result_count': result.result_count, 'language_code': result.language_code, 'indexed': result.indexed,
          'allfromdomain': result.allfromdomain, 'actively_blocked': result.actively_blocked, 'show_sd_ad': result.show_sd_ad,
          'show_network_ad': result.show_network_ad, 'typo_for': result.typo_for, 'is_language': result.is_language,
          'is_language_name': is_language_name, 'superuser': superuser, 'refused': result.refused, 'is_domain': result.is_domain,
          'is_ip': result.is_ip, 'names_language': result.names_language, 'names_language_search': result.names_language_search,
          'names_language_name': names_language_name, 'log': log, 'exclude': exclude, 'date_indexed': result.date_indexed})


@permission_required('is_superuser')
def adminpanel(request):
    result = None
    host = request.META.get('HTTP_HOST', None)
    query_string = request.META.get('QUERY_STRING', None)
    language = LanguageFromDomain(request)
    message = 'You are on host: {0}, language: {1}, request language: {2},  query_string: {3}'.format(host, language, request.LANGUAGE_CODE, query_string)
    if 'crawlurl' in request.GET:
        randomfromdomain = request.GET.get('randomfromdomain', None)
        if not randomfromdomain:
            result = CrawlSingleUrl(request.GET['crawlurl'])
        else:
            # We really should have a way to auto-generate defaults for crawl parameters.
            options = {}
            options['maxurls'] = 1
            options['offset'] = 1
            options['language'] = 'en'
            options['descriptive'] = False
            options['random'] = False
            options['entiredomain'] = request.GET['crawlurl']
            options['pending'] = True
            options['justthisurl'] = False
            options['doctyperecrawl'] = False
            options['xmlfix'] = False
            options['recrawl'] = False
            options['file'] = False
            options['noop'] = False
            options['seconds'] = 0
            result = Crawler(options)
    return render_to_response('adminpanel.htm', {'result': result, 'message': message})


@permission_required('is_superuser')
def adminpanel_movesite(request):
    domain = request.POST.get('domain', None)
    lang = request.POST.get('lang', None)
    if not domain or not lang:
        raise Http404
    pages = SiteInfo.objects.filter(rooturl=domain)
    numpages = 0
    for item in pages:
        MoveSiteTo(item, lang)
        numpages = numpages + 1
    message = 'Moved {0} pages to {1} for domain {2}'.format(numpages, lang, domain)
    return render(request, 'adminpanel.htm', {'message': message})


@permission_required('is_superuser')
def adminpanel_blocksite(request):
    domain = None
    result = None
    sitename = None
    reason = None
    message = None
    if request.method == 'POST':
        sitename = request.POST.get('site', None)
        sitename = GetRootUrl(sitename)
        reason = request.POST.get('reason', None)
        if reason:
            reason = int(reason)
        message = 'Site block requested for {0} for reason {1}. '.format(sitename, reason)
        try:
            domain = DomainInfo.objects.get(url=sitename)
            if domain.is_unblockable:
                message += 'Domain is set as unblockable.'
        except ObjectDoesNotExist:
            # Always create domain info if the domain doesn't exist yet.
            domain = DomainInfo()
            domain.url = sitename
            domain.save()
        try:
            BlockedSite.objects.get(url=sitename)
            # If the domain is already blocked, the URL must have been added erroneously.
            # in that case, just delete it.
            num_before_urls = SiteInfo.objects.filter(rooturl=sitename).count()
            if domain and domain.language_association:
                site_model = GetSiteInfoModelFromLanguage(domain.language_association)
                num_before_urls += site_model.objects.filter(rooturl=sitename).count()
            RemoveURLsForDomain(sitename)
            num_after_urls = SiteInfo.objects.filter(rooturl=sitename).count()
            if domain and domain.language_association:
                num_after_urls += site_model.objects.filter(rooturl=sitename).count()
            RequeueRankedKeywordsForDomain(sitename)
            DeleteDomainLinks(sitename)
            message += 'Domain was already blocked. {0} urls were in the database and now there are {1}.'.format(
                num_before_urls, num_after_urls)
        except ObjectDoesNotExist:
            num_before_urls = SiteInfo.objects.filter(rooturl=sitename).count()
            if domain and domain.language_association:
                site_model = GetSiteInfoModelFromLanguage(domain.language_association)
                num_before_urls += site_model.objects.filter(rooturl=sitename).count()
            site = BlockedSite()
            site.url = sitename
            site.reason = reason
            site.save()
            num_after_urls = SiteInfo.objects.filter(rooturl=sitename).count()
            if domain and domain.language_association:
                num_after_urls += site_model.objects.filter(rooturl=sitename).count()
            RequeueRankedKeywordsForDomain(sitename)
            DeleteDomainLinks(sitename)
            message += 'Domain blocked. {0} urls were in the database and now there are {1}.'.format(
                num_before_urls, num_after_urls)
    elif request.method == 'GET' and 'site' in request.GET:
        sitename = request.GET['site']
        sitename = GetRootUrl(sitename)
        reason = request.GET.get('reason', None)
        message = 'Preparing to block {0}'.format(sitename)
    return render(request, 'adminpanel.htm', {'result': result, 'message': message, 'blocksite': True, 'sitename': sitename,
        'reason': reason, 'choices': EXCLUDED_SITE_REASONS})


@permission_required('is_superuser')
def adminpanel_topsites(request):
    counts = []
    result = None
    cursor = connection.cursor()
    if 'crawlurl' in request.GET:
        result = CrawlSingleUrl(request.GET['crawlurl'])
    for language in language_list:
        if language == 'en':
            limit = 500
        else:
            limit = 100
        model = GetSiteInfoModelFromLanguage(language)
        cursor.execute('SELECT count(*), rooturl FROM ' + model._meta.db_table + ' GROUP BY rooturl ORDER BY count(*) DESC LIMIT ' + str(limit))
        domain_counts = cursor.fetchall()
        counts.append((language, domain_counts))
    return render_to_response('adminpanel.htm', {'domain_counts': counts, 'result': result})


@permission_required('is_superuser')
def adminpanel_pagescore(request):
    url = request.GET.get('url', None)
    keyword = request.GET.get('keyword', None)
    language_code = request.GET.get('language', 'en')
    reasons = None
    elapsed = None
    message = 'Enter a URL and keywords to check {0} {1}.'.format(url, keyword)

    if url and keyword:
        message = 'Results for keywords {0} and url {1}'.format(keyword, url)
        start = timezone.now()
        site_model = GetSiteInfoModelFromLanguage(language_code)
        page = site_model.objects.get(url=url)
        reasons = CalculateTermValue(page, keyword, lang=language_code, verbose=True)
        elapsed = (start - timezone.now()).total_seconds()

    return render(request, 'adminpanel.htm',
        {'reasons': reasons, 'keyword': keyword, 'myurl': url, 'pagescore': True, 'calctime': elapsed, 'message': message})


@permission_required('is_superuser')
def adminpanel_searchlogs(request):
    lang = request.GET.get('lang', 'en')
    maxresults = int(request.GET.get('maxresults', 200))
    unindexed = request.GET.get('unindexed', None)
    twoormore = request.GET.get('twoormore', None)
    threeormore = request.GET.get('threeormore', None)
    zeroresults = request.GET.get('zeroresults', None)
    bingsearches = request.GET.get('bingsearches', None)
    googlesearches = request.GET.get('googlesearches', None)
    slowsearches = request.GET.get('slowsearches', None)
    nodomains = request.GET.get('nodomains', None)
    log_model = GetSearchLogModelFromLanguage(lang)

    if not unindexed:
        logs = log_model.objects.filter(is_bot=False, browserstring__isnull=False).order_by('-last_search')
    else:
        logs = log_model.objects.filter(is_bot=False, browserstring__isnull=False, indexed=False).order_by('-last_search')
    if slowsearches:
        logs = logs.filter(search_time__gte=4)
    if zeroresults:
        logs = logs.filter(result_count=0)
    if twoormore or threeormore:
        logs = logs.filter(keywords__contains=' ')
    if nodomains:
        logs = logs.exclude(keywords__contains=".")
    if bingsearches or googlesearches:
        tmplogs = []
        for log in logs:
            if not log.referer:
                continue
            if bingsearches and 'bing.com' in log.referer:
                tmplogs.append(log)
            if googlesearches and 'google.com' in log.referer:
                tmplogs.append(log)
            if len(tmplogs) > maxresults:
                logs = tmplogs
                break
    if threeormore:
        tmplogs = []
        for log in logs:
            words = log.keywords.split(' ')
            if len(words) > 2:
                tmplogs.append(log)
            if len(tmplogs) > maxresults:
                logs = tmplogs
                break
    else:
        logs = logs[0:maxresults]

    return render(request, 'adminpanel.htm',
        {'message': 'Showing recent non-bot {0} logs'.format(lang), 'logs': logs, 'lang': lang, 'twoormore': twoormore, 'zeroresults': zeroresults,
          'threeormore': threeormore, 'bingsearches': bingsearches, 'googlesearches': googlesearches, 'maxresults': maxresults,
          'unindexed': unindexed, 'nodomains': nodomains})


# Gets a list of the domains with the most URLs that lack a language tag of any kind.
@permission_required('is_superuser')
def adminpanel_unclassified(request):
    counts = []
    uncategorized_domains = []
    cursor = connection.cursor()
    limit = 2500
    cursor.execute('SELECT count(*), rooturl FROM site_info GROUP BY rooturl ORDER BY count(*) DESC LIMIT ' + str(limit))
    domain_counts = cursor.fetchall()
    for domain in domain_counts:
        try:
            domaininfo = DomainInfo.objects.get(url=domain[1])
            if domaininfo.language_association or domaininfo.uses_language_subdirs or domain.uses_langid:
                continue
        except Exception:
            pass
        uncategorized_domains.append(domain)
    counts.append(('en', uncategorized_domains))
    return render_to_response('adminpanel.htm', {'domain_counts': counts})


@permission_required('is_superuser')
def adminpanel_doctype(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'en')
    elif request.method == 'POST':
        lang = request.POST.get('lang', 'en')
    if lang == 'en':
        model_name = 'site_info'
    else:
        model_name = 'dir_siteinfo_' + lang
    cursor = connection.cursor()
    limit = 200
    cursor.execute("SELECT id, lastcrawled, url FROM {0} WHERE pagetext ILIKE 'html public%' LIMIT {1}".format(model_name, limit))
    urls = cursor.fetchall()
    return render_to_response('adminpanel.htm', {'urls': urls, 'lang': lang})


@permission_required('is_superuser')
def adminpanel_oldestcrawls(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'en')
    elif request.method == 'POST':
        lang = request.POST.get('lang', 'en')
    if lang == 'en':
        model_name = 'site_info'
    else:
        model_name = 'dir_siteinfo_' + lang
    cursor = connection.cursor()
    limit = 1000
    cursor.execute("SELECT id, lastcrawled, url FROM {0} ORDER BY lastcrawled ASC LIMIT {1}".format(model_name, limit))
    urls = cursor.fetchall()
    return render_to_response('adminpanel.htm', {'urls': urls, 'lang': lang})


def most_linked_domains(request):
    language_code = request.LANGUAGE_CODE
    cached = False
    if language_code == 'en-us':
        language_code = 'en'

    try:
        stats = IndexStats.objects.all()[0]
    except Exception:
        # Will only happen with an empty database.
        stats = GenerateIndexStats(True)
    try:
        domains = ujson.loads(stats.most_linked_to_domains)
    except ValueError:
        domains = []

    return render_to_response('mostlinked.htm', {'domains': domains, 'cached': cached, 'language_code': language_code})


def popular_searches(request, year=None, month=None):
    language_code = request.LANGUAGE_CODE
    current = False
    cached = False
    if language_code == 'en-us':
        language_code = 'en'
    if not month or not year:
        d = date.today()
        month = d.month
        year = d.year
        current = True
    try:
        report = MonthlySearchReport.objects.get(month=month, year=year, language=language_code)
    except Exception:
        # Only auto-generate the report for the current month.
        if not current:
            raise Http404
        report = cache.get('popular_searches_' + language_code)
        if not report:
            report = GenerateSearchReport(False, month, year, language_code)
            # Cache this report for 6 hours. If this doesn't reduce load enough, we may want
            # to increase it to 24 hours.
            cache.set('popular_searches_' + language_code, report, 172800)
        else:
            cached = True
    month_name = month_names[report.month - 1]
    report.top_searches = ujson.loads(report.top_searches)
    others = MonthlySearchReport.objects.filter(language=language_code).exclude(month=month, year=year)
    return render_to_response('popular.htm', {'report': report, 'language_code': language_code, 'others': others, 'month_name': month_name, 'cached': cached})


def encode_autocomplete(obj):
    return obj.keywords


@csrf_exempt
def autocomplete(request):
    language_code = request.LANGUAGE_CODE
    if language_code == 'en-us':
        language_code = 'en'
    if request.method == 'POST':
        text = request.POST.get('q', None)
        if not text:
            return HttpResponse(status=404)
        autocomplete_model = GetAutoCompleteModelFromLanguage(language_code)
        results = autocomplete_model.objects.filter(keywords__startswith=text).order_by('-score')[0:8]
        if results.count() > 0:
            return HttpResponse((json.dumps(list(results), default=encode_autocomplete)), content_type='application/json', status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=404)


def go(request):
    lang = request.GET.get('lang', None)
    result_model = GetResultClickModelFromLanguage(lang)
    click = result_model()
    click.keywords = request.GET.get('keywords', None)
    click.search_id = request.GET.get('id', None)
    click.url = request.GET.get('url', None)
    click.position = request.GET.get('pos', None)
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        click.ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    elif 'REMOTE_ADDR' in request.META:
        click.ip = request.META['REMOTE_ADDR']
    click.xpos = 0
    click.ypos = 0
    click.save()
    return HttpResponse(status=200)


def error(request):
    raise ValueError('ERROR')


def email(request):
    send_mail('Test Email', 'This is a test message.', 'jchampion@wbsrch.com',
        ['jchampion@sigmacentauri.com'], fail_silently=False)
    return HttpResponse(status=200)


def browser(request):
    return render_to_response('browser.htm')


def getfile(request, filename):
    try:
        print('Looking for file: {0}'.format(filename))
        record = FileDownload.objects.get(filename=filename, enabled=True)
        print('File {0} found'.format(filename))
        record.count = record.count + 1
        record.save()
    except Exception as e:
        print('File not found: {0}.'.format(e))
        return HttpResponseRedirect('/browser/')
    response = HttpResponse()
    response['X-Accel-Redirect'] = '/files/' + filename
    response['Content-Type'] = ""
    print('Redirecting to {0}'.format(response['X-Accel-Redirect']))
    return response
