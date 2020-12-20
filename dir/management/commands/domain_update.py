# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import DomainInfo
import time
import codecs
from dir.domain import UpdateDomainWhois

class Command(BaseCommand):
    help = "This command updates domain whois-related information such as expiration, registrar, etc."
    def add_arguments(self, parser):
        # parser.add_argument('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.')
        parser.add_argument('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Run in verbose mode.')
        # parser.add_argument('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.')
        # parser.add_argument('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).')
        # parser.add_argument('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.')
        parser.add_argument('-j', '--justthisdomain', default=None, action='store', dest='justthisdomain', help='Gets the data for a specific domain')
        parser.add_argument('-m', '--max', default=5, action='store', type=int, dest='max', help='Max number of domains to update. (default=5)')
        parser.add_argument('-s', '--sleep', default=15, action='store', type=int, dest='sleep', help='Time to sleep between domain queries. (default=15)')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)')
        parser.add_argument('-r', '--random', default=False, action='store_true', dest='random', help='Update un-populated domains in random order (default=no)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load domain list from specified file.')
        # TODO: Make an option to fill in nulls vs update already-queried domains.

    def handle(self, *args, **options):
        if options['random']:
            domains = DomainInfo.objects.filter(whois_last_updated__isnull=True).order_by('?')[options['offset']:options['offset'] + options['max']]
        elif options['justthisdomain']:
            domains = DomainInfo.objects.filter(url=options['justthisdomain'])
        elif options['file']:
            filename = options['file']
            domains = []
            numloaded = 0
            print('Loading domains to update from file: {0}'.format(filename))
            f = open(filename, 'rb')
            reader = codecs.getreader('utf8')(f)
            for line in reader.readlines():
                line = line.strip()
                numloaded = numloaded + 1
                try:
                    domain = DomainInfo.objects.get(url=line)
                    domains.append(domain)
                except Exception:
                    # Create domain if not found. This could be problematic if we have a file full of garbage text.
                    print('Domain {0} not found, creating before update.'.format(line))
                    domain = DomainInfo()
                    domain.url = line
                    domain.save()
                    domains.append(domain)
            print('{0} domains loaded from file {1}.'.format(numloaded, filename))
        else:
            domains = DomainInfo.objects.filter(whois_last_updated__isnull=True).order_by('alexa_rank')[options['offset']:options['offset'] + options['max']]
        detailed = options['detailed']
        for domain in domains:
            UpdateDomainWhois(domain, detailed)
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            time.sleep(options['sleep'])
