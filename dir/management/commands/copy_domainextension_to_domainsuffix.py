# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import DomainExtension, DomainSuffix
from dir.utils import GetSiteInfoModelFromLanguage, GetRootUrl
import time

# This management command is no longer needed. It may safely be deleted.

# The purpose was to migrate all domain extensions to the urls database.

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=500, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
    )

    def handle(self, *args, **options):
        ext = DomainExtension.objects.all()[0:options['max']]

        for site in ext:
            new = DomainSuffix()
            new.extension = site.extension
            new.default_language = site.default_language
            new.no_new_domain_urls = site.no_new_domain_urls
            new.save()

        print u'Copied {0} domain extensions to the domain suffix table.'.format(ext.count())
