# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import language_list
from dir.utils import GetSearchLogModelFromLanguage
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = """
    Shows per-language non-bot search totals.
    """

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', action='store', dest='language', default=None, help='Language to check, default = all'),
        parser.add_argument('-d', '--daily', default=False, action='store_true', dest='daily', help='Show daily totals instead of monthly (default=False)'),

    def handle(self, *args, **options):
        if 'language' in options:
            langs = [options['language'], ]
        else:
            langs = language_list
        thirtydaysago = timezone.now() - timedelta(days=30)
        for language in language_list:
            searchlog_model = GetSearchLogModelFromLanguage(language)
            total_searches = searchlog_model.objects.filter(is_bot=False).count()
            print('{0} total searches for {1}'.format(total_searches, language))
            searches_past_month = searchlog_model.objects.filter(is_bot=False, last_search__gte=thirtydaysago).count()
            print('{0} searches in the last 30 days for {1}'.format(searches_past_month, language))
