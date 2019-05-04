
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import BlockedSite
from dir.utils import DeleteDomainLinks
import time
import codecs

class Command(BaseCommand):
    help = """
    Due to redirects and other things, domains don't always have a DomainInfo record when they have URLs
    in the database. This is used to fix that by creating DomainInfo records where they're missing.
    """
    option_list = BaseCommand.option_list + (
        make_option('-s', '--sleep', default=0, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=0)'),
    )

    def handle(self, *args, **options):
        blocked = BlockedSite.objects.all().order_by('url')
        sleep = options.get('sleep', 0)
        processed = 0
        print('{0} blocked sites retrieved.'.format(len(blocked)))
        for item in blocked:
            DeleteDomainLinks(item)
            processed = processed + 1
            if processed % 1000 == 0:
                print('{0} items processed'.format(processed))
            if sleep:
                time.sleep(sleep)

