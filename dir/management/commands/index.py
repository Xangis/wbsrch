# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.indexer import Indexer
from django.conf import settings
from dir.models import language_list
from dir.utils import GetPendingIndexModelFromLanguage


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.')
        parser.add_argument('-b', '--before', default=-1, action='store', dest='days', type=int, help='Only index terms before X days ago. (default=-1)')
        parser.add_argument('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.')
        parser.add_argument('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.')
        parser.add_argument('-i', '--info', default=False, action='store_true', dest='info', help='Print info showing the pendining index counts for all langs and exit.')
        parser.add_argument('-l', '--language', default='en', action='store', dest='language', help='Language to use for pending indexes (default=en).')
        parser.add_argument('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.')
        parser.add_argument('-m', '--maxindexes', default=5, action='store', type=int, dest='maxindexes', help='Max number of terms to index. (default=5)')
        parser.add_argument('-q', '--quickness', default=-1, action='store', type=int, dest='quickness', help='Only works with -r (reindex) and only reindexes terms that took less than X seconds. (default=-1)')
        parser.add_argument('-s', '--sleep', default=2, action='store', type=int, dest='sleep', help='Time to sleep between terms. (default=2)')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Term slice offset - number of items from beginning to start. (default=0)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load term list from specified file.')
        parser.add_argument('-j', '--justthisterm', default=None, action='store', dest='justthisterm', help='Index just this term. Overrides file, pending, or reindex.')
        parser.add_argument('-t', '--type', default='logdivide', action='store', dest='type', help=('Type of indexing to use.'
        'Valid index types are: full, half, loghalf, cuberoot, cuberootb, fourthroot, fourthrootb, logdivide, fourthrootandlog, squareroot1200, squareroot1100, '
        'squareroot1050, squareroot1025, and squareroot1000. (default=logdivide)'))
        parser.add_argument('-x', '--random', default=False, action='store_true', dest='random', help='Select elements in random order.')

    def handle(self, *args, **options):
        if options['verbose']:
            settings.DEBUG = True
        if options['info']:
            for item in language_list:
                pimodel = GetPendingIndexModelFromLanguage(item)
                cnt = pimodel.objects.all().count()
                if cnt:
                    print('{0} pending in {1}'.format(cnt, item))
            exit()
        Indexer(options)
