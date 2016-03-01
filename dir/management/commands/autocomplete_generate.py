# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.utils import GetIndexModelFromLanguage, GetAutoCompleteModelFromLanguage, GetSearchLogModelFromLanguage
from dir.views import language_list
import datetime

class Command(BaseCommand):
    """
    Shows the oldest indexes and/or the oldest index items.
    """
    #option_list = BaseCommand.option_list + (
    #    make_option('-d', '--date', default=None, action='store', type='string', dest='date', help='Date to show old index counts from (default=do not show).'),
    #    make_option('-o', '--oldest', default=False, action='store_true', dest='oldest', help='Show oldest indexes (dfault=False).'),
    #    make_option('-s', '--showempty', default=False, action='store_true', dest='showempty', help='Show empty index counts (use with -d).'),
    #    make_option('-u', '--urls', default=False, action='store_true', dest='showurls', help='Show oldest urls by language.'),
    #)

    def handle(self, *args, **options):
        for language in language_list:
            index_model = GetIndexModelFromLanguage(language)
            autocomplete_model = GetAutoCompleteModelFromLanguage(language)
            searchlog_model = GetSearchLogModelFromLanguage(language)
            items = index_model.objects.filter(actively_blocked=False, refused=False, typo_for__isnull=True, is_language__isnull=True).values('keywords')
            print u'{0} keywords found for {1} language.'.format(items.count(), language)
            print u'Deleting {0} old keywords.'.format(autocomplete_model.objects.all().count())
            autocomplete_model.objects.all().delete()
            print u'Creating new {0} keywords.'.format(language)
            yearago = timezone.now() - datetime.timedelta(days=365)
            for item in items:
                word = autocomplete_model()
                # We could also use number of results.
                #word.score = item.num_results
                # Use the number of non-bot searches as the score for a keyword.
                word.keywords = item['keywords']
                # We should also exclude search engine referrals, but it's a bunch of extra code and doesn't change the
                # results much.
                word.score = searchlog_model.objects.filter(is_bot=False, keywords=word.keywords, last_search__gt=yearago).count()
                word.save()
                print u'Added keyword {0} with {1} score.'.format(word.keywords, word.score)
