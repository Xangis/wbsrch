from django.core.management.base import BaseCommand, CommandError
from dir.utils import BuildJsonIndex
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', action='store', dest='language', default=None, help='The language to generate JSON indexes for'),
        make_option('-m', '--max', action='store', type='int', dest='max', default=100000000, help='Maximum number of terms to generate JSON indexes for.'),
        make_option('-s', '--sleep', action='store', type='int', dest='sleep', default=0, help='The time to sleep between index items.'),
    )

    def handle(self, *args, **options):
        BuildJsonIndex(options['language'], options['max'], sleep=options['sleep'])
