# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.conf import settings
from dir.models import language_list
from dir.utils import GetSearchLogModelFromLanguage
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = "Checks the search logs for new searches in all languages in the past X days and prints them."
    option_list = BaseCommand.option_list + (
        make_option('-d', '--days', default=1, action='store', type='int', dest='days', help='Number of days to query for. (default=1)'),
    )

    def handle(self, *args, **options):
        days = options['days']
        start = timezone.now() - datetime.timedelta(days=days)
        #startdate = '{0}-{1}-{2}'.format(start.year, start.month, start.day)
        for item in language_list:
            logmodel = GetSearchLogModelFromLanguage(item)
            logs = logmodel.objects.filter(indexed=False, is_bot=False, last_search__gte=start).distinct('keywords') #.order_by('-search_time')
            for log in logs:
                print u"{0} (in {1})".format(log.keywords, item)
