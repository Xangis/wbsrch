from django.core.management.base import BaseCommand
from dir.crawler import Crawler
from django.conf import settings


class Command(BaseCommand):
    help = "This is the main command for crawling pages on the web."

    def add_arguments(self, parser):
        # parser.add_argument('-v', '--verbose', default=False, action='store_true', dest='verbose', help='Run in verbose mode.')
        parser.add_argument('-d', '--descriptive', default=False, action='store_true', dest='descriptive', help='Run in descriptive [verbose] mode. (default=False)')
        parser.add_argument('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending URL list from database.')
        parser.add_argument('-e', '--entiredomain', action='store', dest='entiredomain', help='Crawl (or recrawl) and entire domain. Do not use -x with this.')
        parser.add_argument('-m', '--maxurls', default=10, action='store', type=int, dest='maxurls', help='Max number of URLs to crawl. (default=10)')
        parser.add_argument('-s', '--seconds', default=5, action='store', type=int, dest='seconds', help='Seconds to pause between pages. (default=5)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load URL list from specified file.')
        parser.add_argument('-j', '--justthisurl', default=None, action='store', dest='justthisurl', help='Crawls a single URL, specified in the parameter. Use quotes. Always descriptive mode.')
        parser.add_argument('-t', '--doctyperecrawl', default=False, action='store_true', dest='doctyperecrawl', help='Recrawl oldest urls with doctype html public problems from database.')
        parser.add_argument('-z', '--xmlfix', default=False, action='store_true', dest='xmlfix', help='Recrawl oldest urls with xml declaration from.')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Record offset for pending crawl, only works with -p or -r.')
        parser.add_argument('-r', '--recrawl', default=False, action='store_true', dest='recrawl', help='Recrawl oldest existing URLs from database.')
        parser.add_argument('-l', '--language', default=None, action='store', dest='language', help='Language to use for recrawling (default=en). Only works with -r.')
        parser.add_argument('-n', '--noop', default=False, action='store_true', dest='noop', help='Do not crawl the URLs, just list the ones that would be crawled.')
        parser.add_argument('-x', '--random', default=False, action='store_true', dest='random', help='Crawl random URLsr (default=no)')

    def handle(self, *args, **options):
        if options['descriptive']:
            settings.DEBUG = True
        Crawler(options)
