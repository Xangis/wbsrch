# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import SiteInfo
from dir.utils import PornBlock

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-u', '--url', action='store', type='string', dest='url', help='Exact URL to block. Include HTTP/S prefix.'),
    )

    def handle(self, *args, **options):
        if options.has_key('url'):
            url = options['url']
        else:
            print 'ERROR: No URL specified.'
            return
        try:
            info = SiteInfo.objects.get(url=url)
        except ObjectDoesNotExist:
            print 'URL {0} not found. This command only searches the English index.'.format(url)
            return
        PornBlock(info)
