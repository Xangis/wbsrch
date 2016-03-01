# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo, PageLink
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=5, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=5)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-j', '--justthisurl', default=None, action='store', type='string', dest='justthisurl', help='Calculate only for this url.'),
        make_option('-r', '--recalculate', default=False, action='store_true', dest='recalculate', help='Update already-populated domains instead of uncounted (default=False)'),
        make_option('-p', '--popularity', default=False, action='store_true', dest='popularity', help='Sort by popularity before processing. (default=False)'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        sleeptime = options['sleep']
        if options.get('justthisurl', None):
            domains = DomainInfo.objects.filter(url=options['justthisurl'])
        elif options['recalculate']:
            domains = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=False).order_by('domains_linking_in_last_updated')
        else:
            domains = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True)
        if options['popularity']:
            domains = domains.order_by('alexa_rank')
        domains = domains[options['offset']:options['offset']+options['max']]
        for domain in domains:
            num_domains_linking_in = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
            print u'{0} incoming links for {1}'.format(num_domains_linking_in, domain.url)
            domain.domains_linking_in = num_domains_linking_in
            domain.domains_linking_in_last_updated = timezone.now()
            domain.save()
            if sleeptime:
                time.sleep(sleeptime)
        updated = domains.count()
        elapsed = timezone.now() - start
        print u'{0} domains updated in {1} seconds.'.format(updated, elapsed.total_seconds())
