# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import BlockedSite
from dir.utils import RemoveURLsForDomain


class Command(BaseCommand):
    help = """
    This command enforces BlockedSite exclusions on all URLs in the database.

    Domains could be blocked and have pages in the database for various reasons,
    including importing of data, and this goes through and makes sure we don't
    have any pages that we shouldn't.
    """

    def add_arguments(self, parser):
        parser.add_argument('-a', '--all', default=False, action='store_true', dest='all', help='Check all language indexes for blocked site pages (default=False).')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Record offset for check.')

    def handle(self, *args, **options):
        offset = options['offset']
        sites = BlockedSite.objects.all().order_by('url')[offset:]
        count = 0
        for site in sites:
            RemoveURLsForDomain(site.url, verbose=True, all_languages=options['all'])
            count += 1
            if count % 10000 == 0:
                print('Processed {0}'.format(count))
