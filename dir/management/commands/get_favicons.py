# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import DomainInfo
import time
import codecs
from dir.utils import GetFavicons


class Command(BaseCommand):
    help = "This command retrieves favicons for domains."

    def add_arguments(self, parser):
        parser.add_argument('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Run in verbose mode.')
        parser.add_argument('-j', '--justthisdomain', default=None, action='store', dest='justthisdomain', help='Gets the data for a specific domain')
        parser.add_argument('-s', '--sleep', default=5, action='store', type=int, dest='sleep', help='Time to sleep between domain queries. (default=5)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load domain list from specified file.')

    def handle(self, *args, **options):
        if options['justthisdomain']:
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
                except ObjectDoesNotExist:
                    # Create domain if not found. This could be problematic if we have a file full of garbage text.
                    print('Domain {0} not found, creating before favicon harvest.'.format(line))
                    domain = DomainInfo()
                    domain.url = line
                    domain.save()
                    domains.append(domain)
            print('{0} domains loaded from file {1}.'.format(numloaded, filename))
        else:
            print('Must use either -j or -f arguments.')
            return False
        detailed = options['detailed']
        count = 0
        for domain in domains:
            count = count + 1
            if detailed:
                print('Getting favicons for {0}: {1}'.format(count, domain.url))
            if GetFavicons(domain.url):
                print('Retrieved favicons for {0}'.format(domain.url))
            else:
                print('Failed to get favicons for {0}'.format(domain.url))
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            if len(domains) > 1:
                time.sleep(options['sleep'])
