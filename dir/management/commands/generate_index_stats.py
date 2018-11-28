from django.core.management.base import BaseCommand, CommandError
from dir.utils import GenerateIndexStats

class Command(BaseCommand):
    def handle(self, *args, **options):
        stats = GenerateIndexStats(True, True)
        print 'Done. ' + str(stats.total_urls) + ' URLs crawled, ' + str(stats.total_indexes) + ' terms indexed, ' + str(stats.total_pendingindexes) + ' indexes pending, and ' + str(stats.num_excluded) + ' excluded sites.'
