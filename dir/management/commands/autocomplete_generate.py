# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils import timezone
from dir.utils import GetIndexModelFromLanguage, GetAutoCompleteModelFromLanguage, GetSearchLogModelFromLanguage
from dir.views import language_list
import datetime


class Command(BaseCommand):
    help = """
    Generates autocomplete data based on search popularity in the search logs for all languages. This takes a long time, and autocomplete
    will be broken for the currently running languages because it deletes all existing autocompletes first.
    """
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for language in language_list:
            index_model = GetIndexModelFromLanguage(language)
            autocomplete_model = GetAutoCompleteModelFromLanguage(language)
            searchlog_model = GetSearchLogModelFromLanguage(language)
            items = index_model.objects.filter(actively_blocked=False, refused=False, typo_for__isnull=True, is_language__isnull=True).values('keywords')
            print('{0} keywords found for {1} language.'.format(items.count(), language))
            print('Deleting {0} old keywords.'.format(autocomplete_model.objects.all().count()))
            autocomplete_model.objects.all().delete()
            print('Creating new {0} keywords.'.format(language))
            yearago = timezone.now() - datetime.timedelta(days=365)
            for item in items:
                word = autocomplete_model()
                # We could also use number of results.
                # word.score = item.num_results
                # Use the number of non-bot searches as the score for a keyword.
                word.keywords = item['keywords']
                # We should also exclude search engine referrals, but it's a bunch of extra code and doesn't change the
                # results much.
                word.score = searchlog_model.objects.filter(is_bot=False, keywords=word.keywords, last_search__gt=yearago).count()
                word.save()
                print('Added keyword {0} with {1} score.'.format(word.keywords, word.score))
