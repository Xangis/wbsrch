# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list
from dir.utils import GetIndexAverageAge, GetOldestIndexAge, GetIndexModelFromLanguage
from django.utils.timezone import utc
from dateutil.parser import parse


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default='all', action='store', dest='language', help='Language to use for index ages, or "all" for all. (default=all).')
        parser.add_argument('-d', '--days', default=None, action='store', type=int, dest='days', help='If specified, only prints details for languages older than this number of days.')
        parser.add_argument('-b', '--before', default=None, action='store', type=str, dest='before', help='If specified, only shows counts that are older than the specified date.')

    def handle(self, *args, **options):
        days = options.get('days', None)
        before = options.get('before', None)
        if before:
            before = parse(before)
            before = before.replace(tzinfo=utc)
        if options['language'] == 'all':
            for item in language_list:
                if before:
                    model = GetIndexModelFromLanguage(item)
                    total = model.objects.filter(date_indexed__lt=before).count()
                    if total:
                        print('There are {0} index terms for "{1}" that are older than {2}'.format(total, item, before))
                else:
                    age = GetIndexAverageAge(item)
                    if days and (age.days < days):
                        continue
                    print('Index "{0}" has average age of {1}, oldest is {2}.'.format(
                          item, age, GetOldestIndexAge(item)))
        else:
            if before:
                model = GetIndexModelFromLanguage(item)
                total = model.objects.filter(date_indexed__lt=before).count()
                print('There are {0} index terms for "{1}" that are older than {2}'.format(total, item, before))
            else:
                age = GetIndexAverageAge(options['language'])
                print('Index "{0}" has average age of {1}, oldest is {2}.'.format(
                      options['language'], age, GetOldestIndexAge(options['language'])))
