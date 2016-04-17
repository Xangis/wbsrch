# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink, BlockedSite
import time
import codecs

class Command(BaseCommand):
    help = "Checks link and block data to create a list of domains that are probably porn."
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=100, action='store', type='int', dest='max', help='Max number of domains to check. (default=100)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Check the URLs in the specified file.'),
        make_option('-s', '--sleep', default=0, action='store', type='int', dest='sleep', help='Time to sleep between domain checks. (default=0)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        file = options.get('file', None)
        if file:
            print u'Not implemented yet. Come back later.'
            print u'Using file {0}.'.format(file)
            f = open(file, 'rb')
            reader = codecs.getreader('utf8')(f)
            sources = reader.readlines()
            total = len(sources)
        else:
            sources = PageLink.objects.all().values('rooturl_source').distinct().order_by('rooturl_source')[options['offset']:options['offset']+options['max']]
            total = sources.count()
        definitely_porn = []
        probably_porn = []
        possibly_porn = []
        print u'Checking as many as {1} starting with {2}. Retrieved {0}.'.format(total, options['max'], options['offset'])
        for source in sources:
            porndomains = 0
            thisstart = timezone.now()
            if file:
                domain = source.strip()
            else:
                domain = source['rooturl_source']
            print 'Domain: {0}'.format(domain)
            try:
                excluded = BlockedSite.objects.get(url=domain)
                print u'Domain {0} already excluded, no need to check.'.format(domain)
                continue
            except ObjectDoesNotExist:
                pass
            destinations = PageLink.objects.filter(rooturl_source=domain).values('rooturl_destination').distinct()
            for destination in destinations:
                try:
                    excluded = BlockedSite.objects.get(url=destination['rooturl_destination'], reason=4)
                    print u'Domain {0} links to {1}, which is blocked as porn.'.format(domain, destination['rooturl_destination'])
                    porndomains = porndomains + 1
                    continue
                except ObjectDoesNotExist:
                    pass
            thisend = timezone.now() - thisstart
            if porndomains > 0:
                print u'Domain {0} links to {1} porn domains, calculated in {2} seconds.'.format(domain, porndomains, thisend.total_seconds())
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
            if porndomains > 4:
                definitely_porn.append((domain, language, rank))
            elif porndomains > 2:
                probably_porn.append((domain, language, rank))
            elif porndomains > 0:
                possibly_porn.append((domain, language, rank))
            if options['sleep'] > 0:
                time.sleep(options['sleep'])
        definitely_porn = sorted(definitely_porn, key=lambda item: item[2], reverse=False)
        probably_porn = sorted(probably_porn, key=lambda item: item[2], reverse=False)
        possibly_porn = sorted(possibly_porn, key=lambda item: item[2], reverse=False)
        print u'--- THESE DOMAINS ARE POSSIBLY PORN ---'
        for domainurl in possibly_porn:
            if domainurl[1] == 'en':
                print u'{1} http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl[0], domainurl[2])
            else:
                print u'{2} http://wbsrch.com/adm/dir/siteinfo_{0}/?q={1}'.format(domainurl[1], domainurl[0], domainurl[2])
        print u'--- THESE DOMAINS ARE PROBABLY PORN ---'
        for domainurl in probably_porn:
            if domainurl[1] == 'en':
                print u'{1} http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl[0], domainurl[2])
            else:
                print u'{2} http://wbsrch.com/adm/dir/siteinfo_{0}/?q={1}'.format(domainurl[1], domainurl[0], domainurl[2])
        print u'--- THESE DOMAINS ARE DEFINITELY PORN ---'
        for domainurl in definitely_porn:
            if domainurl[1] == 'en':
                print u'{1} http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl[0], domainurl[2])
            else:
                print u'{2} http://wbsrch.com/adm/dir/siteinfo_{0}/?q={1}'.format(domainurl[1], domainurl[0], domainurl[2])
        elapsed = timezone.now() - start
        print u'Task completed in {0} seconds.'.format(elapsed.total_seconds())
