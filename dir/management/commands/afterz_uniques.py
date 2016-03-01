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
        make_option('-o', '--oldest', default=False, action='store_true', dest='oldest', help='Show oldest indexes (dfault=False).'),
        make_option('-s', '--showempty', default=False, action='store_true', dest='showempty', help='Show empty index counts (use with -d).'),
    )

    def handle(self, *args, **options):
        items = SiteInfoAfterZ.objects.filter(pagetitle__gt='ZZZZZZZZZZ').order_by('rooturl')
        #items = SiteInfoAfterZ.objects.filter(pagetitle__lt='0').order_by('rooturl')
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
                        roots.append(item.rooturl)
        print u'Num roots: {0}'.format(len(roots))
        for root in roots:
            print root
