# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo
from dir.domain import GetDomainAge
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        #make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        #make_option('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.'),
        #make_option('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.'),
        #make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        #make_option('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.'),
        make_option('-j', '--justthisdomain', default=None, action='store', type='string', dest='justthisdomain', help='Gets the data for a specific domain'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=15, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=15)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-r', '--random', default=False, action='store_true', dest='random', help='Update un-populated domains in random order (default=no)'),
        #make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),

        # TODO: Make an option to fill in nulls vs update already-queried domains.
    )

    def handle(self, *args, **options):
        if options['random']:
            domains = DomainInfo.objects.filter(expiration_last_updated__isnull=True).order_by('?')[options['offset']:options['offset']+options['max']]
        elif options['justthisdomain']:
            domains = DomainInfo.objects.filter(url=options['justthisdomain'])
        else:
            domains = DomainInfo.objects.filter(expiration_last_updated__isnull=True).order_by('alexa_rank')[options['offset']:options['offset']+options['max']]
        for domain in domains:
            print 'Updating {0}'.format(domain.url)
            ages = GetDomainAge(domain.url)
            if ages[0] != None or ages[1] != None:
                domain.domain_created = ages[0]
                domain.domain_expires = ages[1]
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            domain.expiration_last_updated = timezone.now()
            domain.save()
            time.sleep(options['sleep'])
