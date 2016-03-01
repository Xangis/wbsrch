# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import ExcludedSite, BlockedSite
from dir.utils import GetSiteInfoModelFromLanguage, GetRootUrl
import time

# This management command is no longer needed. It may safely be deleted.

# The purpose was to fix all mis-rooturled-domains that had http in the rooturl.

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for domains (default=en). It is dumb to use not english because if a domain is in another table, it has been categorized and has a domain info.'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=15, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=15)'),
    )

    def handle(self, *args, **options):
        excluded = ExcludedSite.objects.all()
        for site in excluded:
            new = BlockedSite()
            new.url = site.url
            new.reason = site.reason
            new.detailedreason = site.detailedreason
            new.exclude_subdomains = site.exclude_subdomains
            new.save(remove=False)

        print u'Copied {0} excluded sites to the blocked site table.'.format(excluded.count())
