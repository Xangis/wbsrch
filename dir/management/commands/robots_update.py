# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from optparse import make_option
from dir.models import DomainInfo
from dir.robots import GetRobotsFile
import time


class Command(BaseCommand):
    help = "Daemon to query the robots.txt file for domains."
    option_list = BaseCommand.option_list + (
        # make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        # make_option('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.'),
        # make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        make_option('-j', '--justthisdomain', default=None, action='store', type='string', dest='justthisdomain', help='Gets the robots.txt for a specific domain. Overrides all crawl types.'),
        make_option('-i', '--ipcrawl', default=False, action='store_true', dest='ipcrawl', help='Get domains with missing IP addresses (overrides recrawl, random, and popularity, and works in random order like -x)'),
        make_option('-r', '--recrawl', default=False, action='store_true', dest='recrawl', help='Re-get existing least-recently-updated robots files. Does not work with -i'),
        make_option('-p', '--popularity', default=False, action='store_true', dest='popularity', help='Do this in order of popularity. Does not work with -i.'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=5, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=5)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-x', '--random', default=False, action='store_true', dest='random', help='Update un-populated domains in random order (default=no). Automatic with -i.'),
        # make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),

        # TODO: Make an option to fill in nulls vs update already-queried domains.
    )

    def handle(self, *args, **options):
        if options['justthisdomain']:
            domains = DomainInfo.objects.filter(url=options['justthisdomain'])
        elif options['ipcrawl']:
            domains = DomainInfo.objects.filter(robots_ip__isnull=True).order_by('?')[options['offset']:options['offset'] + options['max']]
        elif options['recrawl']:
            domains = DomainInfo.objects.filter(robots_last_updated__isnull=False).order_by('robots_last_updated')[options['offset']:options['offset'] + options['max']]
        elif options['random']:
            domains = DomainInfo.objects.filter(robots_last_updated__isnull=True).order_by('?')[options['offset']:options['offset'] + options['max']]
        elif options['popularity']:
            domains = DomainInfo.objects.filter(robots_last_updated__isnull=True).order_by('alexa_rank')[options['offset']:options['offset'] + options['max']]
        else:
            domains = DomainInfo.objects.filter(robots_last_updated__isnull=True)[options['offset']:options['offset'] + options['max']]
        for domain in domains:
            GetRobotsFile(domain, True, save_failures=True)
            time.sleep(options['sleep'])
