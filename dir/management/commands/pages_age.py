# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list
from dir.utils import GetPagesAverageAge, GetOldestPageAge, GetSiteInfoModelFromLanguage


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default='all', action='store', dest='language', help='Language to use for index ages, or "all" for all. (default=all).')
        parser.add_argument('-d', '--days', default=None, action='store', type=int, dest='days', help='If specified, only prints details for languages older than this number of days.')
        parser.add_argument('-b', '--before', default=None, action='store', type=str, dest='before', help='If specified, only shows counts that are older than the specified date.')

    def handle(self, *args, **options):
        days = options.get('days', None)
        before = options.get('before', None)
        if options['language'] == 'all':
            for item in language_list:
                if before:
                    model = GetSiteInfoModelFromLanguage(item)
                    total = model.objects.filter(lastcrawled__lt=before).count()
                    print('There are {0} pages for "{1}" that are older than {2}'.format(total, item, before))
                else:
                    age = GetPagesAverageAge(item)
                    if days and (age.days < days):
                        continue
                    print('Pages for "{0}" have average age of {1} days, oldest is {2}.'.format(
                          item, age, GetOldestPageAge(item)))
        else:
            if before:
                model = GetSiteInfoModelFromLanguage(item)
                total = model.objects.filter(lastcrawled__lt=before).count()
                print('There are {0} pages for "{1}" that are older than {2}'.format(total, item, before))
            else:
                age = GetPagesAverageAge(options['language'])
                print('Pages for "{0}" have average age of {1} days, oldest is {2}.'.format(
                      options['language'], age, GetOldestPageAge(options['language'])))
