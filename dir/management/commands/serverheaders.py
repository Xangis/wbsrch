from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option
from dir.models import Setting
import urllib2

class Command(BaseCommand):
    help = "Gets the web server headers for a URL."
    option_list = BaseCommand.option_list + (
        #make_option('-v', '--verbose', default=False, action='store_true', dest='verbose', help='Run in verbose mode.')
        make_option('-d', '--descriptive', default=False, action='store_true', dest='descriptive', help='Run in descriptive [verbose] mode. (default=False)'),
        make_option('-j', '--justthisurl', default=None, action='store', type='string', dest='justthisurl', help='Crawls a single URL, specified in the parameter. Use quotes.'),
    )

    def handle(self, *args, **options):
        url = options['justthisurl']
        print u'Retrieving ' + unicode(url)
        req = urllib2.Request(url)
        try:
            user_agent = Setting.objects.get(name='wbsrch_user_agent')
            req.add_header('User-agent', user_agent.value)
        except ObjectDoesNotExist:
            req.add_header('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0')
        try:
            response = urllib2.urlopen(req, timeout=20)
        except:
            print u'Failed to retrieve URL.'

        info = response.info()
        print info
        idict = dict(info)
        print idict        
        print u'Server = {0}'.format(idict.get('server', None))
        print u'Content Type = {0}'.format(idict.get('content-type', None))
        print idict['server']
        print idict['content-type']
