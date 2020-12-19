# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections
from django.core.management.base import BaseCommand
from optparse import make_option
from dir.utils import GetIndexModelFromLanguage


class Command(BaseCommand):
    help = """
    This command examines existing indexes for sparse-result (<5 by default) terms and looks for similar words with
    a larger number of results to see if the sparse term might be a typo for the well-populated term.

    If you get an error saying that levenshtein does not exist, you need to CREATE EXTENSION fuzzystrmatch; on the indexes database.
    """
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        make_option('-d', '--distance', default=1, action='store', type='int', dest='distance', help='Levenshtein distance to check. (default=1)'),
        make_option('-u', '--under', default=5, action='store', type='int', dest='under', help='Check terms with fewer than this many results. (default=5)'),
        make_option('-o', '--over', default=1000, action='store', type='int', dest='over', help='Min number of results to consider as a possible intent. (default=1000)'),
        make_option('-s', '--skip', default=0, action='store', type='int', dest='skip', help='Number of items to skip. (default=0)'),
        make_option('-n', '--nonumbers', default=False, action='store_true', dest='nonumbers', help='Do not check terms containing numbers.'),
    )

    def handle(self, *args, **options):
        language = options.get('language', None)
        distance = options.get('distance', 0)
        under = options.get('under', 0)
        over = options.get('over', 0)
        skip = options.get('skip', 0)
        nonumbers = options.get('nonumbers', False)
        index_model = GetIndexModelFromLanguage(language)
        check = index_model.objects.filter(num_results__lt=under, typo_for__isnull=True, refused=False).order_by('keywords')[skip:]
        print('Found {0} items to check.'.format(check.count()))
        for pos, item in enumerate(check):
            if nonumbers and any(i.isdigit() for i in item.keywords):
                continue
            print('{1}: Checking {0}'.format(item.keywords, pos + skip))
            cursor = connections['indexes'].cursor()
            cursor.execute("SELECT keywords, num_results FROM dir_indexterm WHERE KEYWORDS != %s AND num_results > {1} AND levenshtein(keywords, %s) <= {0} ORDER BY num_results DESC;".format(distance, over), [item.keywords, item.keywords])
            possible_words = cursor.fetchall()
            for word in possible_words:
                print(word)
            if len(possible_words) < 1:
                print('No matches found, skipping.')
                continue
            if len(possible_words) == 1:
                word = str(possible_words[0])
                # Adding or removing an S is not a match.
                if (item.keywords + u's') == word:
                    print('No matches found, skipping.')
                    continue
                if (word + u's') == item.keywords:
                    print('No matches found, skipping.')
                    continue
            input = raw_input(u'Enter correct word, s to skip, q to quit: ')
            input = input.lower()
            if input == 'q':
                quit()
            elif input == 's' or len(input) < 2:
                continue
            else:
                print('Setting "{0}" as typo_for on {1}'.format(input, item.keywords))
                item.typo_for = input
                item.save()
