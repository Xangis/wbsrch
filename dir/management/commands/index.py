# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.indexer import Indexer
from django.conf import settings
from dir.models import language_list
from dir.utils import GetPendingIndexModelFromLanguage

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        make_option('-b', '--before', default=-1, action='store', dest='days', type='int', help='Only index terms before X days ago. (default=-1)'),
        make_option('-d', '--detailed', default=False, action='store_true', dest='verbose', help='Run in verbose mode.'),
        make_option('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.'),
        make_option('-i', '--info', default=False, action='store_true', dest='info', help='Print info showing the pendining index counts for all langs and exit.'),
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        make_option('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.'),
        make_option('-m', '--maxindexes', default=5, action='store', type='int', dest='maxindexes', help='Max number of terms to index. (default=5)'),
        make_option('-q', '--quickness', default=-1, action='store', type='int', dest='quickness', help='Only works with -r (reindex) and only reindexes terms that took less than X seconds. (default=-1)'),
        make_option('-s', '--sleep', default=2, action='store', type='int', dest='sleep', help='Time to sleep between terms. (default=2)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Term slice offset - number of items from beginning to start. (default=0)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),
        make_option('-j', '--justthisterm', default=None, action='store', type='string', dest='justthisterm', help='Index just this term. Overrides file, pending, or reindex.'),
        make_option('-t', '--type', default='fourthrootandlog', action='store', type='string', dest='type', help=('Type of indexing to use. '
        'Valid index types are: full, half, loghalf, cuberoot, cuberootb, fourthroot, fourthrootb, logdivide, fourthrootandlog, squareroot1200, squareroot1100, '
        'squareroot1050, squareroot1025, and squareroot1000. (default=fourthrootandlog)')),
        make_option('-x', '--random', default=False, action='store_true', dest='random', help='Select elements in random order.'),
    )

    def handle(self, *args, **options):
        if options['verbose']:
            settings.DEBUG = True
        if options['info']:
            for item in language_list:
                pimodel = GetPendingIndexModelFromLanguage(item)
                cnt = pimodel.objects.all().count()
                if cnt:
                    print u'{0} pending in {1}'.format(cnt, item)
            exit()
        Indexer(options)
