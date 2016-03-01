# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import URLLink, PageLink
from dir.utils import GetSiteInfoModelFromLanguage, GetRootUrl
import time

# This management command is no longer needed. It may safely be deleted.

# Tehe purpose was to migrate all URLLinks to the PageLink model.

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=1000000, action='store', type='int', dest='max', help='Max number of items to copy. (default=1000000)'),
    )

    def handle(self, *args, **options):
        params = URLLink.objects.all()
        for site in params:
            new = PageLink()
            new.rooturl_source = site.rooturl_source
            new.url_source = site.url_source
            new.rooturl_destination = site.rooturl_destination
            new.url_destination = site.url_destination
            new.anchor_text = site.anchor_text
            new.save()

        print u'Copied {0} URL links to the page link table.'.format(params.count())
