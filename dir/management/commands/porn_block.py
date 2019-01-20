# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import SiteInfo
from dir.utils import PornBlock, GetRootUrl
import codecs

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-u', '--url', action='store', type='string', dest='url', help='Exact URL to block. Include HTTP/S prefix.'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load domain list from specified file.'),
    )

    def handle(self, *args, **options):
        urls = []
        if options['file']:
            filename = options['file']
            numloaded = 0
            print('Loading domains to porn block from file: {0}'.format(filename))
            f = open(filename, 'rb')
            reader = codecs.getreader('utf8')(f)
            for line in reader.readlines():
                urls.append(line)
        elif options.has_key('url'):
            urls.append = options['url'].strip()
        else:
            print 'ERROR: No URL specified.'
            return

        print('Blocking {0} domains.'.format(len(urls)))
        for url in urls:
            url = GetRootUrl(url.strip())
            print('Blocking "{0}".'.format(url))
            PornBlock(url=url)
