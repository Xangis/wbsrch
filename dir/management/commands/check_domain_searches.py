# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.models import *
from dir.utils import *

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

class Command(BaseCommand):
    help = """Checks search results for domain names and prints a list of domains that need to be crawled. However, this command is
              not particularly useful because most domain name searches are spam domains."""

    option_list = BaseCommand.option_list + (
        make_option('-w', '--websearches', default=False, action='store_true', dest='websearches', help='Check web searches for domains instead of checking domain searches.'),
    )

    def handle(self, *args, **options):
        maxurls = options.get('maxurls', 100000)
        websearches = options.get('websearches', False)
        if websearches:
            print u'Getting web search data.'
            searches = SearchLog.objects.filter(keywords__contains='.', is_bot=False, indexed=False).order_by('keywords')
        else:
            print u'Getting domain search data.'
            searches = DomainSearchLog.objects.filter(is_bot=False, result_count=0, indexed=False).order_by('keywords')
        print u'{0} searches found. Analyzing domains for crawl status.'.format(searches.count())
        unknown_domains = []
        for domain in searches:
            domain.keywords = domain.keywords.lower()
            if '=' in domain.keywords:
                continue
            if '+' in domain.keywords:
                continue
            if ' ' in domain.keywords:
                continue
            if '\\' in domain.keywords:
                continue
            if '\t' in domain.keywords:
                continue
            if '\v' in domain.keywords:
                continue
            if "'" in domain.keywords:
                continue
            if "(" in domain.keywords:
                continue
            if ")" in domain.keywords:
                continue
            if '\n' in domain.keywords:
                domain.keywords = domain.keywords.replace('\n', '')
            if '"' in domain.keywords:
                domain.keywords = domain.keywords.replace('"', '')
            if domain.keywords.startswith('.'):
                continue
            if domain.keywords.endswith('.'):
                continue
            if domain.keywords.startswith('#'):
                domain.keywords = domain.keywords[1:]
            if domain.keywords.startswith('@'):
                domain.keywords = domain.keywords[1:]
            if '@' in domain.keywords:
                continue
            if domain.keywords.startswith('site:'):
                domain.keywords = domain.keywords[5:]
            if domain.keywords.startswith('http://'):
                domain.keywords = domain.keywords[7:]
            if domain.keywords.startswith('https://'):
                domain.keywords = domain.keywords[8:]
            if '/' in domain.keywords:
                pieces = domain.keywords.split('/')
                domain.keywords = pieces[0]
            if not '.' in domain.keywords:
                continue
            if "&" in domain.keywords:
                continue
            if IsIPAddress(domain.keywords):
                continue
            if domain.keywords.endswith('.php') or domain.keywords.endswith('.js') or domain.keywords.endswith('.exe') or domain.keywords.endswith('.txt') or domain.keywords.endswith('.aspx') or domain.keywords.endswith('.htm') or domain.keywords.endswith('.html'):
                continue
            pieces = domain.keywords.split('.')
            if len(pieces[-1]) < 2:
                continue
            if HasNumber(pieces[-1]):
                continue
            found = False
            for piece in pieces:
                if len(piece) > 1:
                    found = True
            if not found:
                continue
            # Domain name must be ASCII or it's invalid.
            if not is_ascii(domain.keywords):
                continue
            try:
                blockedsite = BlockedSite.objects.get(url=domain.keywords)
                continue
            except ObjectDoesNotExist:
                pass
            try:
                domaininfo = DomainInfo.objects.get(url=domain.keywords)
                continue
            except ObjectDoesNotExist:
                pass
            if domain.keywords not in unknown_domains:
                unknown_domains.append(domain.keywords)
        if not websearches:
            print u'Re-getting domain search data for update.'
            searches = DomainSearchLog.objects.filter(is_bot=False, result_count=0, indexed=False).order_by('keywords')
            print u'Domains checked. Marking all queried domains as indexed (which means it has been checked)'
            for domain in searches:
                domain.indexed = True
                domain.save()
        print u'{0} domains need to be crawled.'.format(len(unknown_domains))
        for domain in unknown_domains:
            print domain
