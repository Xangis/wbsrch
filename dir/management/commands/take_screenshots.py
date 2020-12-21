# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import DomainInfo
import time
import codecs
from dir.utils import TakeScreenshot

class Command(BaseCommand):
    help = "This command takes screenshots of home pages for domains."

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
                    print('Domain {0} not found, creating before screenshot.'.format(line))
                    domain = DomainInfo()
                    domain.url = line
                    domain.save()
                    domains.append(domain)
            print('{0} domains loaded from file {1}.'.format(numloaded, filename))
        else:
            print('Must use either -j or -f arguments.')
            return False
        detailed = options['detailed']
        for domain in domains:
            if detailed:
                print('Taking screenshot of {0}'.format(domain.url))
            if TakeScreenshot(domain.url):
                print('Took screenshot of {0}'.format(domain.url))
            else:
                print('Failed to take screenshot of {0}'.format(domain.url))
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            if len(domains) > 1:
                time.sleep(options['sleep'])
