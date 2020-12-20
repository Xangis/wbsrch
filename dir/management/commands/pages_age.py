# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list
from dir.utils import GetPagesAverageAge, GetOldestPageAge


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default='all', action='store', dest='language', help='Language to use for index ages, or "all" for all. (default=all).')
        parser.add_argument('-d', '--days', default=None, action='store', type=int, dest='days', help='If specified, only prints details for languages older than this number of days.')

    def handle(self, *args, **options):
        days = options.get('days', None)
        if options['language'] == 'all':
            for item in language_list:
                age = GetPagesAverageAge(item)
                if days and (age.days < days):
                    continue
                print('Pages for "{0}" have average age of {1} days, oldest is {2}.'.format(
                      item, age, GetOldestPageAge(item)))
        else:
            age = GetPagesAverageAge(options['language'])
            print('Pages for "{0}" have average age of {1} days, oldest is {2}.'.format(
                  options['language'], age, GetOldestPageAge(options['language'])))
