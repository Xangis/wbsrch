# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink, BlockedSite
import time
import operator

class Command(BaseCommand):
    help = "Checks link and block data to create a list of domains that are probably in languages that we don't index."
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=100, action='store', type='int', dest='max', help='Max number of domains to check. (default=100)'),
        make_option('-s', '--sleep', default=0, action='store', type='int', dest='sleep', help='Time to sleep between domain checks. (default=0)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        sources = PageLink.objects.all().values('rooturl_source').distinct().order_by('rooturl_source')[options['offset']:options['offset']+options['max']]
        definitely_unindexed = []
        probably_unindexed = []
        possibly_unindexed = []
        blockedlinkcounts = {}
        total = sources.count()
        print u'Checking as many as {1} starting with {2}. Retrieved {0}.'.format(total, options['max'], options['offset'])
        for source in sources:
            unindexeddomains = 0
            thisstart = timezone.now()
            domain = source['rooturl_source']
            print 'Domain: {0}'.format(domain)
            try:
                excluded = BlockedSite.objects.get(url=domain)
                print u'Domain {0} already blocked, no need to check.'.format(domain)
                continue
            except ObjectDoesNotExist:
                pass
            destinations = PageLink.objects.filter(rooturl_source=domain).values('rooturl_destination').distinct()
            for destination in destinations:
                try:
                    dest = destination['rooturl_destination']
                    excluded = BlockedSite.objects.get(url=dest, reason=8)
                    print u'Domain {0} links to {1}, which is blocked as unindexed language.'.format(domain, dest)
                    unindexeddomains = unindexeddomains + 1
                    if blockedlinkcounts.has_key(dest):
                        blockedlinkcounts[dest] = blockedlinkcounts[dest] + 1
                    else:
                        blockedlinkcounts[dest] = 1
                    continue
                except ObjectDoesNotExist:
                    pass
            thisend = timezone.now() - thisstart
            if unindexeddomains > 5:
                print u'Domain {0} links to {1} unindexed lang domains, calculated in {2} seconds.'.format(domain, unindexeddomains, thisend.total_seconds())
                definitely_unindexed.append(domain)
            elif unindexeddomains > 3:
                print u'Domain {0} links to {1} unindexed lang domains, calculated in {2} seconds.'.format(domain, unindexeddomains, thisend.total_seconds())
                probably_unindexed.append(domain)
            elif unindexeddomains > 1:
                print u'Domain {0} links to {1} unindexed lang domains, calculated in {2} seconds.'.format(domain, unindexeddomains, thisend.total_seconds())
                possibly_unindexed.append(domain)
            else:
                pass
                #print u'Domain {0} is clean, calculated in {1} seconds.'.format(domain, thisend.total_seconds())
            if options['sleep'] > 0:
                time.sleep(options['sleep'])
        print u'--- THESE DOMAINS ARE POSSIBLY UNINDEXED LANGUAGE ---'
        for domainurl in possibly_unindexed:
            print u'http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl)
        print u'--- THESE DOMAINS ARE PROBABLY UNINDEXED LANGUAGE ---'
        for domainurl in probably_unindexed:
            print u'http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl)
        print u'--- THESE DOMAINS ARE DEFINITELY UNINDEXED LANGUAGE ---'
        for domainurl in definitely_unindexed:
            print u'http://wbsrch.com/adm/dir/siteinfo/?q={0}'.format(domainurl)
        topblocked = sorted(blockedlinkcounts.iteritems(), key=operator.itemgetter(1), reverse=True)
        print u"--- THESE DOMAINS SHOULD BE CHECKED TO MAKE SURE THEY REALLY SHOULD BE BLOCKED ---"
        for item in topblocked[0:20]:
            print u'({0}) {1}'.format(item[1], item[0])
        elapsed = timezone.now() - start
        print u'Task completed in {0} seconds.'.format(elapsed.total_seconds())
