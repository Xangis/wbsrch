from django.core.management.base import BaseCommand
from dir.utils import GenerateIndexStats


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-n', '--nolinks', default=False, action='store_true', dest='nolinks', help='Do not regenerate most-linked-to-domain lists even if it is due.')

    def handle(self, *args, **options):
        stats = GenerateIndexStats(True, True, options['nolinks'])
        print('Done. ' + str(stats.total_urls) + ' URLs crawled, ' + str(stats.total_indexes) + ' terms indexed, ' + str(stats.total_pendingindexes) + ' indexes pending, and ' + str(stats.num_excluded) + ' excluded sites.')
