# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.indexer import Indexer
from django.conf import settings
from dir.models import language_list
from dir.utils import GetIndexAverageAge, GetOldestIndexAge

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='all', action='store', type='string', dest='language', help='Language to use for index ages, or "all" for all. (default=all).'),
        make_option('-d', '--days', default=None, action='store', type='int', dest='days', help='If specified, only prints details for languages older than this number of days.'),
    )

    def handle(self, *args, **options):
        days = options.get('days', None)
        if options['language'] == 'all':
            for item in language_list:
                age = GetIndexAverageAge(item)
                if days and (age.days < days):
                    continue
                print('Index "{0}" has average age of {1}, oldest is {2}.'.format(
                      item, age, GetOldestIndexAge(item)))
        else:
            age = GetIndexAverageAge(options['language'])
            print('Index "{0}" has average age of {1}, oldest is {2}.'.format(
                  options['language'], age, GetOldestIndexAge(options['language'])))
