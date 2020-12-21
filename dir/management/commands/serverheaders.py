from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import Setting
import urllib.request
import urllib.error
import urllib.parse


class Command(BaseCommand):
    help = "Gets the web server headers for a URL."

    def add_arguments(self, parser):
        # parser.add_argument('-v', '--verbose', default=False, action='store_true', dest='verbose', help='Run in verbose mode.')
        parser.add_argument('-d', '--descriptive', default=False, action='store_true', dest='descriptive', help='Run in descriptive [verbose] mode. (default=False)')
        parser.add_argument('-j', '--justthisurl', default=None, action='store', dest='justthisurl', help='Crawls a single URL, specified in the parameter. Use quotes.')

    def handle(self, *args, **options):
        url = options['justthisurl']
        print('Retrieving ' + str(url))
        req = urllib.request.Request(url)
        try:
            user_agent = Setting.objects.get(name='wbsrch_user_agent')
            req.add_header('User-agent', user_agent.value)
        except ObjectDoesNotExist:
            req.add_header('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0')
        try:
            response = urllib.request.urlopen(req, timeout=20)
        except Exception:
            print('Failed to retrieve URL.')

        info = response.info()
        print(info)
        idict = dict(info)
        print(idict)
        print('Server = {0}'.format(idict.get('server', None)))
        print('Content Type = {0}'.format(idict.get('content-type', None)))
        print(idict['server'])
        print(idict['content-type'])
