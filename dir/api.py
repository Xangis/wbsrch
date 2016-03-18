# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, Http404, HttpResponseForbidden, HttpResponseBadRequest
from django.db.models import get_model, Count
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
    if not domain.startswith(u'http:') or domain.startswith(u'https:'):
        parsedurl = urlparse(domain)
        parseddomain = parsedurl.geturl()
        domain = parsedurl.netloc
    return domain

@api_view(['GET'])
def ip_to_country(request):
    if not request.auth:
        return HttpResponse(status=403)
    else:
        print 'ip_to_country called by {0}'.format(request.user)
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
        return HttpResponse(status=403)
    else:
        print 'domain_link_rank called by {0}'.format(request.user)
    domain = request.GET.get('domain', None)
    if not domain:
        return Response(status=404)
    domain = NormalizeDomain(domain)
    print 'Domain: {0}'.format(domain)
    try:
        domaininfo = DomainInfo.objects.get(url=domain)
    except ObjectDoesNotExist:
        return Response(status=404)
    is_excluded = False
    try:
        excluded = BlockedSite.objects.get(url=domain)
        is_excluded = True
    except ObjectDoesNotExist:
        pass
    link_rank = GetLinkRank(domaininfo.domains_linking_in)
    # Round to the nearest integer because we don't want to give too much precision away.
    link_rank = int(round(link_rank))
    # TODO: Include domains_linking_in_last_updated in response.
    return Response({'domain': domain, 'wbrank': link_rank, 'excluded': is_excluded}, status=200)

@api_view(['GET'])
def domain_pages_in_index(request):
    if not request.auth:
        return HttpResponse(status=403)
    domain = request.GET.get('domain', None)
    print 'Domain: {0}'.format(domain)
    return Response({'domain': domain }, status=200)

@api_view(['GET'])
def domain_keywords_ranked(request):
    if not request.auth:
        return HttpResponse(status=403)
    domain = request.GET.get('domain', None)
    print 'Domain: {0}'.format(domain)
    return Response({'domain': domain }, status=200)

@api_view(['GET'])
def autocomplete(request):
    if not request.auth:
        return HttpResponse(status=403)
    word = request.GET.get('word', None)
    print 'Word: {0}'.format(word)
    return Response({'word': word}, status=200)

@api_view(['GET'])
def check_typo(request):
    if not request.auth:
        return HttpResponse(status=403)
    word = request.GET.get('word', None)
    print 'Word: {0}'.format(word)
    return Response({'word': word}, status=200)
