# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import SiteInfoAfterZ, SiteInfo
from dir.utils import GetRootUrl
import dateutil.parser

class Command(BaseCommand):
    """
    Shows the oldest indexes and/or the oldest index items.
    """
    option_list = BaseCommand.option_list + (
        make_option('-e', '--extension', action='store', dest='extension', help='Check files with this extension instead of afterz.'),
        make_option('-z', '--beforezero', default=False, action='store_true', dest='beforezero', help='Check before zero instead of afterz. (default=No)'),
        make_option('-1', '--h1', default=False, action='store_true', dest='h1', help='Check h1 instead of title. (default=No)'),
        make_option('-2', '--h2', default=False, action='store_true', dest='h2', help='Check h2 instead of title. (default=No)'),
        make_option('-3', '--h3', default=False, action='store_true', dest='h3', help='Check h3 instead of title. (default=No)'),
    )

    def handle(self, *args, **options):
        extension = options.get('extension', None)
        h1 = options.get('h1', None)
        h2 = options.get('h2', None)
        h3 = options.get('h3', None)
        if extension:
            items = SiteInfo.objects.filter(rooturl__endswith=extension).order_by('rooturl')
        elif options.get('beforezero', None):
            if h1:
                items = SiteInfoAfterZ.objects.filter(pagefirstheadtag__lt='0', pagefirstheadtag__gt=' ').order_by('rooturl')
            elif h2:
                items = SiteInfoAfterZ.objects.filter(pagefirsth2tag__lt='0', pagefirsth2tag__gt=' ').order_by('rooturl')
            elif h3:
                items = SiteInfoAfterZ.objects.filter(pagefirsth3tag__lt='0', pagefirsth3tag__gt=' ').order_by('rooturl')
            else:
                items = SiteInfoAfterZ.objects.filter(pagetitle__lt='0', pagetitle__gt=' ').order_by('rooturl')
        else:
            if h1:
                items = SiteInfoAfterZ.objects.filter(pagefirstheadtag__gt='ZZZZZZZZZZ').order_by('rooturl')
            elif h2:
                items = SiteInfoAfterZ.objects.filter(pagefirsth2tag__gt='ZZZZZZZZZZ').order_by('rooturl')
            elif h3:
                items = SiteInfoAfterZ.objects.filter(pagefirsth3tag__gt='ZZZZZZZZZZ').order_by('rooturl')
            else:
                items = SiteInfoAfterZ.objects.filter(pagetitle__gt='ZZZZZZZZZZ').order_by('rooturl')
        print u'Num items: {0}'.format(items.count())
        roots = []
        for item in items:
            if not item.rooturl in roots:
                try:
                    info = SiteInfo.objects.get(url='http://' + item.rooturl)
                except ObjectDoesNotExist:
                    try:
                        info = SiteInfo.objects.get(url='http://' + item.rooturl + '/')
                    except ObjectDoesNotExist:
                        try:
                            info = SiteInfo.objects.get(url='https://' + item.rooturl + '/')
                        except ObjectDoesNotExist:
                            try:
                                info = SiteInfo.objects.get(url='https://' + item.rooturl)
                            except ObjectDoesNotExist:
                                roots.append(item.rooturl)
        print u'Num roots: {0}'.format(len(roots))
        for root in roots:
            print root
