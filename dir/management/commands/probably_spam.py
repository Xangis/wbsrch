# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink, BlockedSite
import time

class Command(BaseCommand):
    help = "Checks link and block data to create a list of domains that are probably spam."
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=100, action='store', type='int', dest='max', help='Max number of domains to check. (default=100)'),
        make_option('-s', '--sleep', default=0, action='store', type='int', dest='sleep', help='Time to sleep between domain checks. (default=0)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        sources = PageLink.objects.all().values('rooturl_source').distinct().order_by('rooturl_source')[options['offset']:options['offset']+options['max']]
        possibly_spam = []
        definitely_spam = []
        total = sources.count()
        print('Checking as many as {1} starting with {2}. Retrieved {0}.'.format(total, options['max'], options['offset']))
        for source in sources:
            spamdomains = 0
            thisstart = timezone.now()
            domain = source['rooturl_source']
            print('Domain: {0}'.format(domain))
            try:
                excluded = BlockedSite.objects.get(url=domain)
                print('Domain {0} already excluded, no need to check.'.format(domain))
                continue
            except ObjectDoesNotExist:
                pass
            destinations = PageLink.objects.filter(rooturl_source=domain).values('rooturl_destination').distinct()
            for destination in destinations:
                try:
                    excluded = BlockedSite.objects.get(url=destination['rooturl_destination'], reason=7)
                    print('Domain {0} links to {1}, which is blocked as spam.'.format(domain, destination['rooturl_destination']))
                    spamdomains = spamdomains + 1
                    continue
                except ObjectDoesNotExist:
                    pass
            thisend = timezone.now() - thisstart
            if spamdomains > 0:
                print('Domain {0} links to {1} spam domains, calculated in {2} seconds.'.format(domain, spamdomains, thisend.total_seconds()))
            language = 'en'
            rank = 9999999
            try:
                dom = DomainInfo.objects.get(url=domain)
                if dom.language_association:
                    language = dom.language_association
                if dom.alexa_rank:
                    rank = dom.alexa_rank
            except ObjectDoesNotExist:
                pass
            if spamdomains > 3:
                definitely_spam.append((domain, language, rank))
            elif spamdomains > 0:
                possibly_spam.append((domain, language, rank))
            if options['sleep'] > 0:
                time.sleep(options['sleep'])
        definitely_spam = sorted(definitely_spam, key=lambda item: item[2], reverse=False)
        possibly_spam = sorted(possibly_spam, key=lambda item: item[2], reverse=False)
        print('--- THESE DOMAINS ARE POSSIBLY SPAM ---')
        for domainurl in possibly_spam:
            if domainurl[1] == 'en':
                print('{1} http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl[0], domainurl[2]))
            else:
                print('{2} http://wbsrch.com/adm/dir/siteinfo_{0}/?q={1}'.format(domainurl[1], domainurl[0], domainurl[2]))
        print('--- THESE DOMAINS ARE DEFINITELY SPAM ---')
        for domainurl in definitely_spam:
            if domainurl[1] == 'en':
                print('{1} http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl[0], domainurl[2]))
            else:
                print('{2} http://wbsrch.com/adm/dir/siteinfo_{0}/?q={1}'.format(domainurl[1], domainurl[0], domainurl[2]))
        elapsed = timezone.now() - start
        print('Task completed in {0} seconds.'.format(elapsed.total_seconds()))
