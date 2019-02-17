# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from optparse import make_option
from dir.models import DomainInfo
from dir.domain import GetDomainInfo
from django.db.utils import DataError
import time
import codecs
from dir.utils import GetFavicons

class Command(BaseCommand):
    help = "This command retrieves favicons for domains."

    option_list = BaseCommand.option_list + (
        make_option('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Run in verbose mode.'),
        make_option('-j', '--justthisdomain', default=None, action='store', type='string', dest='justthisdomain', help='Gets the data for a specific domain'),
        make_option('-s', '--sleep', default=5, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=5)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load domain list from specified file.'),
    )

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
                except:
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
        for domain in domains:
            if detailed:
                print('Getting favicons for {0}'.format(domain.url))
            if GetFavicons(domain.url):
                print('Retrieved favicons for {0}'.format(domain.url))
            else:
                print('Failed to get favicons for {0}'.format(domain.url))
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            if len(domains) > 1:
                time.sleep(options['sleep'])
