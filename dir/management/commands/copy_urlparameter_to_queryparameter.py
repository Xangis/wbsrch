# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import URLParameter, QueryParameter
from dir.utils import GetSiteInfoModelFromLanguage, GetRootUrl
import time

# This management command is no longer needed. It may safely be deleted.

# The purpose was to fix all mis-rooturled-domains that had http in the rooturl.

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=1000000, action='store', type='int', dest='max', help='Max number of items to copy. (default=1000000)'),
    )

    def handle(self, *args, **options):
        params = URLParameter.objects.all()
        for site in params:
            new = QueryParameter()
            new.parameter = site.parameter
            new.domain = site.domain
            new.remove_before_crawl = site.remove_before_crawl
            new.replace_before_crawl = site.replace_before_crawl
            new.remove_or_replace_after_crawl = site.remove_or_replace_after_crawl
            new.only_replace_if_present = site.only_replace_if_present
            new.save()

        print u'Copied {0} URL parameters to the query parameters table.'.format(params.count())
