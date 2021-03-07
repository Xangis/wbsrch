# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from dir.models import APISubscription, APIUsage, APIUser, APIToken, BlockedSite, DomainInfo, SiteInfo, EXCLUDED_SITE_REASONS
from dir.utils import GetLinkRank, ReverseWWW
from dir.domain import UpdateDomainWhois
from urllib.parse import urlparse
from django.contrib.gis.geoip import GeoIP
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import get_authorization_header
import hashlib
import uuid
import binascii


# Note: In order to use the API, the user must have both a valid token AND
# a valid subscription entered in the admin.


def CreateToken(user):
    # We may want to use a better salt, but at least we're not using b'salt'.
    dk = hashlib.pbkdf2_hmac('sha256', str(uuid.uuid4()).encode(), b'saltedcaramel', 250000)
    key = binascii.hexlify(dk).decode()[0:36]
    print('New API token for APIUser {0} ({1}): {2}'.format(user.name, user.id, key))
    token = APIToken()
    token.key = key
    token.save()


def GetToken(request):
    auth = get_authorization_header(request).split()
    if not auth or auth[0].lower() != b'token':
        msg = "Invalid request: No API token supplied."
        raise exceptions.AuthenticationFailed(msg)

    if len(auth) == 1:
        msg = 'Invalid token header. No credentials provided.'
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth) > 2:
        msg = 'Invalid token header'
        raise exceptions.AuthenticationFailed(msg)

    try:
        token = auth[1]
        if token == "null":
            msg = 'Null token not allowed'
            raise exceptions.AuthenticationFailed(msg)
    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        raise exceptions.AuthenticationFailed(msg)

    # Query database for token.
    apitoken = APIToken.objects.get(key=token)
    return apitoken


def NormalizeDomain(domain):
    # Normalize URL
    if domain.startswith('http:') or domain.startswith('https:'):
        parsedurl = urlparse(domain)
        parsedurl.geturl()
        domain = parsedurl.netloc
    return domain


def SwapHttps(url):
    if url.startswith('http:'):
        url = 'https:' + url[5:]
    elif url.startswith('https:'):
        url = 'http:' + url[6:]
    return url


def IncrementAPICallCount(user):
    """
    Increments the monthly API call count for a user. Returns True if
    successful, False if the user either doesn't have a valid subscription,
    or if the call count has been exceeded.
    """
    time = timezone.now()
    try:
        subscription = APISubscription.objects.get(user=user, expires__gte=time)
    except ObjectDoesNotExist:
        return False
    try:
        usage = APIUsage.objects.get(user=user, month=time.month, year=time.year)
    except ObjectDoesNotExist:
        usage = APIUsage()
        apiuser = APIUser.objects.get(id=user.id)
        if not apiuser:
            apiuser = APIUser()
            apiuser.userid = user.id
            apiuser.name = user.name
        usage.user = apiuser
        usage.month = time.month
        usage.year = time.year
    if usage.calls_used < subscription.monthly_calls:
        usage.calls_used = usage.calls_used + 1
        usage.save()
        return True
    else:
        return False


@api_view(['GET'])
def ip_to_country(request):
    token = GetToken(request)

    print('ip_to_country called by {0}'.format(token.user.name))
    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)

    ip = request.GET.get('ip', None)
    print('IP: {0}'.format(ip))
    gi = GeoIP()
    country = gi.country_code(ip)
    latlon = gi.lat_lon(ip)
    if country and latlon:
        return Response({'ip': ip, 'country': country, 'lat': latlon[0], 'lon': latlon[1]}, status=200)
    elif country:
        return Response({'ip': ip, 'country': country}, status=200)
    else:
        return Response(status=404)


@api_view(['GET'])
def domain_link_rank(request):
    token = GetToken(request)

    print('domain_link_rank called by {0}'.format(request.user))
    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    decimal = request.GET.get('decimal', None)
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    print('Domain: {0}'.format(domain))
    altdomain = ReverseWWW(domain, False)
    domainfound = False
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        domainfound = True
    except ObjectDoesNotExist:
        pass
    is_excluded = False
    excluded_reason = None
    try:
        excluded = BlockedSite.objects.get(url=domain)
        is_excluded = True
        excluded_reason = 'Unknown'
        for reason in EXCLUDED_SITE_REASONS:
            if reason[0] == excluded.reason:
                excluded_reason = reason[1]
                break
    except ObjectDoesNotExist:
        pass
    if domainfound:
        domains_linking_in = domaininfo.domains_linking_in
    else:
        domains_linking_in = 0
    altdomain = ReverseWWW(domain, False)
    if altdomain:
        print('Altdomain is {0}'.format(altdomain))
        try:
            altdomaininfo = DomainInfo.objects.get(url=altdomain)
            # Handle Nones temporarily.
            if not altdomaininfo.domains_linking_in:
                altdomaininfo.domains_linking_in = 0
            print('Alt domain DomainInfo found')
            domainfound = True
            if not domains_linking_in:
                domains_linking_in = 0
            print('{0} domains linking in to domain {1} and {2} linking in to {3} for a total of {4}'.format(domains_linking_in,
                domain, altdomaininfo.domains_linking_in, altdomain, domains_linking_in + altdomaininfo.domains_linking_in))
            domains_linking_in += altdomaininfo.domains_linking_in
        except ObjectDoesNotExist:
            pass
    elif domainfound:
        print('{0} domains linking in to domain {1}'.format(domains_linking_in, domain))
    if not domainfound:
        return Response({'error': 'Domain {0} not found.'.format(domain)}, status=404)
    link_rank = GetLinkRank(domains_linking_in)
    # Round to the nearest integer because we don't want to give too much precision away.
    if not decimal:
        link_rank = int(round(link_rank))
    if link_rank > 8:
        link_rank = 8
    # TODO: Include domains_linking_in_last_updated in response.
    return Response({'domain': domain, 'wbrank': link_rank, 'excluded': is_excluded, 'domains_linking_in': domains_linking_in, 'excluded_reason': excluded_reason}, status=200)


@api_view(['GET'])
def domain_pages_in_index(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    altdomain = ReverseWWW(domain, False)
    print('Domain: {0}'.format(domain))
    domainfound = False
    altdomainfound = False
    domaininfo = None
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        domainfound = True
    except ObjectDoesNotExist:
        pass
    if altdomain:
        try:
            altdomaininfo = DomainInfo.objects.get(url=altdomain)
            altdomainfound = True
        except ObjectDoesNotExist:
            pass

    pages = 0
    if domainfound and domaininfo.num_urls:
        pages += domaininfo.num_urls
        print('{0} urls for domain {1}'.format(domaininfo.num_urls, domain))
    if altdomainfound and altdomaininfo.num_urls:
        pages += altdomaininfo.num_urls
        print('{0} urls for altdomain {1}'.format(altdomaininfo.num_urls, altdomain))

    # TODO: Make the num_pages_in_index calculation take language association into account.
    # if domaininfo and not (domaininfo.language_association or (domaininfo.language_association == 'en')):
    #    return Response({'domain': domain, 'total_pages_crawled': pages, 'en': pages}, status=200)
    # elif domaininfo:
    #    return Response({'domain': domain, 'total_pages_crawled': pages, domaininfo.language_association: pages}, status=200)
    # else:
    return Response({'domain': domain, 'total_pages_crawled': pages, 'en': pages}, status=200)


@api_view(['GET'])
def domain_keywords_ranked(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    # language = request.GET.get('lang', 'en')
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    altdomain = ReverseWWW(domain, False)
    print('Domain: {0}'.format(domain))
    domainfound = False
    altdomainfound = False
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        domainfound = True
    except ObjectDoesNotExist:
        pass
    if altdomain:
        try:
            altdomaininfo = DomainInfo.objects.get(url=domain)
            altdomainfound = True
        except ObjectDoesNotExist:
            pass

    keywords = 0
    if domainfound and domaininfo.num_keywords_ranked:
        keywords += domaininfo.num_keywords_ranked
        print('{0} keywords for domain {1}'.format(domaininfo.num_keywords_ranked, domain))
    if altdomainfound and altdomaininfo.num_keywords_ranked:
        keywords += altdomaininfo.num_keywords_ranked
        print('{0} keywords for altdomain {1}'.format(altdomaininfo.num_keywords_ranked, altdomain))

    # TODO: Make the calculations language-aware.
    # return Response({'domain': domain, '{0}_ranked'.format(language): keywords}, status=200)
    return Response({'domain': domain, 'en_ranked': keywords}, status=200)


@api_view(['GET'])
def autocomplete(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    word = request.GET.get('word', None)
    print('Word: {0}'.format(word))
    return Response({'word': word}, status=200)


@api_view(['GET'])
def check_typo(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    word = request.GET.get('word', None)
    print('Word: {0}'.format(word))
    return Response({'word': word}, status=200)


# Gets the full page info for a URL (number of javascript and CSS items, size, etc.)
@api_view(['GET'])
def get_page_details(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    page = request.GET.get('page', None)
    if not page.startswith('http'):
        page = 'https://{0}'.format(page)
    # TODO: Try both HTTP and HTTPS, check DomainInfo to see what language index should be queried.
    # TODO: Try to crawl the page if it doesn't exist yet (depending on account permissions -- some accounts should and some should not be
    # allowed to trigger url retreival with this call.
    try:
        pageinfo = SiteInfo.objects.get(url=page)
        return Response({'page': page, 'url': pageinfo.url, 'domain': pageinfo.rooturl, 'title': pageinfo.pagetitle, 'description': pageinfo.pagedescription,
          'ip': pageinfo.ip, 'num_css_files': pageinfo.num_css_files, 'num_images': pageinfo.num_images, 'num_javascript_files': pageinfo.num_javascripts,
          'num_iframes': pageinfo.num_iframes, 'num_audio_tags': pageinfo.num_audio_tags, 'num_video_tags': pageinfo.num_video_tags, 'num_svg_tags': pageinfo.num_svg_tags,
          'num_canvas_tags': pageinfo.num_canvas_tags, 'image_filenames': pageinfo.image_filenames, 'content_type': pageinfo.content_type_header,
          'server_header': pageinfo.server_header, 'retrieved_time': pageinfo.lastcrawled, 'size': pageinfo.pagesize}, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'Page {0} not found in index.'.format(page)}, status=404)

    """
    Things we're not currently retrieving (and may or may not want to):
    pagefirstheadtag = models.CharField(max_length=260, blank=True, null=True)
    pagefirsth2tag = models.CharField(max_length=260, blank=True, null=True)
    pagefirsth3tag = models.CharField(max_length=260, blank=True, null=True)
    pagekeywords = models.CharField(max_length=260, blank=True, null=True)
    pagetext = models.TextField(blank=True, null=True)
    firstcrawled = models.DateTimeField(null=True, blank=True) # Note that this won't be accurate for pages recrawled before 2015-09-22.
    num_errors = models.IntegerField(blank=True, default=0)
    error_info = models.TextField(blank=True, default='')
    image_alt_tags = models.TextField(null=True, blank=True)
    image_title_tags = models.TextField(null=True, blank=True)
    """


# Gets the Alexa, Majestic, Quantcast, and Domcop rank for a domain (from whenever we had it last). Leaves unranked ones blank.
@api_view(['GET'])
def get_ranks(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    domain = NormalizeDomain(domain)
    print('Domain: {0}'.format(domain))
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        return Response({'domain': domain, 'alexa_rank': domaininfo.alexa_rank, 'alexa_rank_date': domaininfo.alexa_rank_date,
                         'majestic_rank': domaininfo.majestic_rank, 'majestic_rank_date': domaininfo.majestic_rank_date,
                         'domcop_pagerank': domaininfo.domcop_pagerank, 'domcop_pagerank_date': domaininfo.domcop_pagerank_date, 'domcop_rank': domaininfo.domcop_rank,
                         'quantcast_rank': domaininfo.quantcast_rank, 'quantcast_rank_date': domaininfo.quantcast_rank_date
                        }, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'Domain {0} not found.'.format(domain)}, status=404)


# Gets the whois info for a domain if we have it.
@api_view(['GET'])
def get_whois_info(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    domain = NormalizeDomain(domain)
    print('Domain: {0}'.format(domain))
    # TODO: Query the domain if it does not have whois_last_updated set.
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        if not domaininfo.whois_last_updated:
            UpdateDomainWhois(domaininfo)
        return Response({'domain': domain, 'domain_created': domaininfo.domain_created, 'domain_expires': domaininfo.domain_expires, 'domain_last_updated': domaininfo.domain_updated,
          'info_updated': domaininfo.whois_last_updated, 'whois_name': domaininfo.whois_name, 'whois_city': domaininfo.whois_city, 'whois_country': domaininfo.whois_country,
          'whois_state': domaininfo.whois_state, 'whois_address': domaininfo.whois_address, 'whois_org': domaininfo.whois_org, 'whois_registrar': domaininfo.whois_registrar,
          'whois_zipcode': domaininfo.whois_zipcode, 'whois_nameservers': domaininfo.whois_nameservers, 'whois_emails': domaininfo.whois_emails}, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'Domain {0} not found.'.format(domain)}, status=404)


# Gets the robots.txt info for a domain if we have it.
@api_view(['GET'])
def get_robots_info(request):
    token = GetToken(request)

    if not IncrementAPICallCount(token.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    domain = NormalizeDomain(domain)
    print('Domain: {0}'.format(domain))
    # TODO: Query the domain if it does not have robots_last_updated set.
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        return Response({'domain': domain, 'robots_ip': domaininfo.robots_ip, 'robots_txt': domaininfo.robots_txt, 'robots_last_updated': domaininfo.robots_last_updated}, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'Domain {0} not found.'.format(domain)}, status=404)
