# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, Http404, HttpResponseForbidden, HttpResponseBadRequest
from django.db.models import Count
from django.db import connection
from django.core.cache import cache
from django.utils import timezone
import json
from models import *
from utils import *
from language import language_name_reverse
from crawler import CrawlSingleUrl, Crawler
from urlparse import urlparse
from datetime import datetime, date, timedelta
from django.contrib.gis.geoip import GeoIP
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

def get_token(user):
    token = Token.objects.create(user=user)
    print token.key
    token.save()

def NormalizeDomain(domain):
    # Normalize URL
    if domain.startswith(u'http:') or domain.startswith(u'https:'):
        parsedurl = urlparse(domain)
        parseddomain = parsedurl.geturl()
        domain = parsedurl.netloc
    return domain

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
        usage.user = user
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
    if not request.auth:
        return HttpResponse(status=403)
    else:
        print 'ip_to_country called by {0}'.format(request.user)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    ip = request.GET.get('ip', None)
    print 'IP: {0}'.format(ip)
    gi = GeoIP()
    country = gi.country_code(ip)
    latlon = gi.lat_lon(ip)
    if country and latlon:
        return Response({'ip': ip, 'country': country, 'lat': latlon[0], 'lon': latlon[1] }, status=200)
    elif country:
        return Response({'ip': ip, 'country': country }, status=200)
    else:
        return Response(status=404)

@api_view(['GET'])
def domain_link_rank(request):
    if not request.auth:
        return HttpResponse({'error': 'Not authorized.'}, status=403)
    else:
        print 'domain_link_rank called by {0}'.format(request.user)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    decimal = request.GET.get('decimal', None)
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    print 'Domain: {0}'.format(domain)
    altdomain = ReverseWWW(domain, False)
    domainfound = False
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        domainfound = True
    except ObjectDoesNotExist:
        pass
    is_excluded = False
    try:
        excluded = BlockedSite.objects.get(url=domain)
        is_excluded = True
    except ObjectDoesNotExist:
        pass
    if domainfound:
        domains_linking_in = domaininfo.domains_linking_in
    else:
        domains_linking_in = 0
    altdomain = ReverseWWW(domain, False)
    if altdomain:
        print u'Altdomain is {0}'.format(altdomain)
        try:
            altdomaininfo = DomainInfo.objects.get(url=altdomain)
            print 'Alt domain DomainInfo found'
            domainfound = True
            print u'{0} domains linking in to domain {1} and {2} linking in to {3} for a total of {4}'.format(domains_linking_in,
                domain, altdomaininfo.domains_linking_in, altdomain, domains_linking_in + altdomaininfo.domains_linking_in)
            domains_linking_in += altdomaininfo.domains_linking_in
        except ObjectDoesNotExist:
            pass
    elif domainfound:
        print u'{0} domains linking in to domain {1}'.format(domains_linking_in, domain)
    if not domainfound:
        return Response({'error': 'Domain {0} not found.'.format(domain)}, status=404)
    link_rank = GetLinkRank(domains_linking_in)
    # Round to the nearest integer because we don't want to give too much precision away.
    if not decimal:
        link_rank = int(round(link_rank))
    if link_rank > 8:
        link_rank = 8
    # TODO: Include domains_linking_in_last_updated in response.
    return Response({'domain': domain, 'wbrank': link_rank, 'excluded': is_excluded}, status=200)

@api_view(['GET'])
def domain_pages_in_index(request):
    if not request.auth:
        return HttpResponse(status=403)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    altdomain = ReverseWWW(domain, False)
    print 'Domain: {0}'.format(domain)
    domainfound = False
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
        domainfound = True
        site_model = GetSiteInfoModelFromLanguage(domaininfo.language_association)
    except ObjectDoesNotExist:
        site_model = SiteInfo
        pass
    pages = site_model.objects.filter(rooturl=domain).count()
    if altdomain:
        added = site_model.objects.filter(rooturl=altdomain).count()
        print u'{0} pages for domain {1} and {2} pages for domain {3} for a total of {4}'.format(pages, domain, added, altdomain, pages+added)
        pages += added
    else:
        print u'{0} pages for domain {1}'.format(pages, domain)
    if site_model == SiteInfo:
        return Response({'domain': domain, 'total': pages, 'en': pages }, status=200)
    else:
        return Response({'domain': domain, 'total': pages, domaininfo.language_association: pages }, status=200)

@api_view(['GET'])
def domain_keywords_ranked(request):
    if not request.auth:
        return HttpResponse(status=403)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    domain = request.GET.get('domain', None)
    if not domain:
        return Response({'error': 'Domain query parameter is required.'}, status=400)
    domain = NormalizeDomain(domain)
    altdomain = ReverseWWW(domain, False)
    print 'Domain: {0}'.format(domain)
    keywords = KeywordRanking.objects.filter(rooturl=domain, rank__lt=200).count()
    if altdomain:
        added = KeywordRanking.objects.filter(rooturl=altdomain, rank__lt=200).count()
        print u'{0} keywords for domain {1} and {2} keywords for domain {3} for a total of {4}'.format(keywords, domain, added, altdomain, keywords+added)
        keywords += added
    else:
        print u'{0} keywords for domain {1}'.format(keywords, domain)
    return Response({'domain': domain, 'en': keywords }, status=200)

@api_view(['GET'])
def autocomplete(request):
    if not request.auth:
        return HttpResponse(status=403)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    word = request.GET.get('word', None)
    print 'Word: {0}'.format(word)
    return Response({'word': word}, status=200)

@api_view(['GET'])
def check_typo(request):
    if not request.auth:
        return HttpResponse(status=403)
    if not IncrementAPICallCount(request.user):
        return HttpResponse('Account exceeded API call limit or does not have active subscription.', status=403)
    word = request.GET.get('word', None)
    print 'Word: {0}'.format(word)
    return Response({'word': word}, status=200)
