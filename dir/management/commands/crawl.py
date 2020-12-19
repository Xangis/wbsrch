from django.core.management.base import BaseCommand
from optparse import make_option
from dir.crawler import Crawler
from django.conf import settings


class Command(BaseCommand):
    help = "This is the main command for crawling pages on the web."

    option_list = BaseCommand.option_list + (
        # make_option('-v', '--verbose', default=False, action='store_true', dest='verbose', help='Run in verbose mode.')
        make_option('-d', '--descriptive', default=False, action='store_true', dest='descriptive', help='Run in descriptive [verbose] mode. (default=False)'),
        make_option('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending URL list from database.'),
        make_option('-e', '--entiredomain', action='store', type='string', dest='entiredomain', help='Crawl (or recrawl) and entire domain. Do not use -x with this.'),
        make_option('-m', '--maxurls', default=10, action='store', type='int', dest='maxurls', help='Max number of URLs to crawl. (default=10)'),
        make_option('-s', '--seconds', default=5, action='store', type='int', dest='seconds', help='Seconds to pause between pages. (default=5)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load URL list from specified file.'),
        make_option('-j', '--justthisurl', default=None, action='store', type='string', dest='justthisurl', help='Crawls a single URL, specified in the parameter. Use quotes. Always descriptive mode.'),
        make_option('-t', '--doctyperecrawl', default=False, action='store_true', dest='doctyperecrawl', help='Recrawl oldest urls with doctype html public problems from database.'),
        make_option('-z', '--xmlfix', default=False, action='store_true', dest='xmlfix', help='Recrawl oldest urls with xml declaration from.'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Record offset for pending crawl, only works with -p or -r.'),
        make_option('-r', '--recrawl', default=False, action='store_true', dest='recrawl', help='Recrawl oldest existing URLs from database.'),
        make_option('-l', '--language', default=None, action='store', type='string', dest='language', help='Language to use for recrawling (default=en). Only works with -r.'),
        make_option('-n', '--noop', default=False, action='store_true', dest='noop', help='Do not crawl the URLs, just list the ones that would be crawled.'),
        make_option('-x', '--random', default=False, action='store_true', dest='random', help='Crawl random URLsr (default=no)'),
    )

    def handle(self, *args, **options):
        if options['descriptive']:
            settings.DEBUG = True
        Crawler(options)
