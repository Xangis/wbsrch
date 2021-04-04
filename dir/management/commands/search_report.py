# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list
from dir.utils import GetSearchLogModelFromLanguage
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = """
    Shows per-language non-bot search totals.
    """

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', action='store', dest='language', default='all', help='Language(s) to check, comma-separated, default = all'),
        parser.add_argument('-d', '--daily', default=False, action='store_true', dest='daily', help='Show daily totals instead of monthly (default=False)'),

    def handle(self, *args, **options):
        if options['language'] == 'all':
            langs = language_list
        else:
            langs = options['language'].split(',')
        thirtydaysago = timezone.now() - timedelta(days=30)
        for language in langs:
            searchlog_model = GetSearchLogModelFromLanguage(language)
            total_searches = searchlog_model.objects.filter(is_bot=False).count()
            searches_past_month = searchlog_model.objects.filter(is_bot=False, last_search__gte=thirtydaysago).count()
            print('{0} searches in the last 30 days and {1} all-time searches for {2}'.format(searches_past_month, total_searches, language))
