# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.language import NLTKLanguageDetect, IdentifyPageLanguage, IdentifyLanguage

class Command(BaseCommand):
    help = """Tool for semi-manual or keyword language categorization."""

    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Two-letter lowercase language code to check'),
    )

    def handle(self, *args, **options):
        language = options['language']
        result = None
        cursor = connection.cursor()
        cursor2 = connection.cursor()
        uncategorized_domains = []
        # We start with the domains having the most pages and descend.
        cursor.execute("SELECT keyword, num_results FROM dir_indexterm WHERE (is_language IS NULL or is_language='') AND actively_blocked = false AND (typo_for IS NULL or typo_for='') ORDER BY num_results DESC")
        keywords = cursor.fetchall()
        for keyword in keywords:
            language_results = {}
            print('Checking Keyword: {0}'.format(keyword))
            for language in language_list:
                if language == 'en':
                    cursor2.execute('SELECT keyword, num_results FROM dir_indexterm WHERE keyword IS {0}'.format(keyword['keyword']))
                else:
                    cursor2.execute('SELECT keyword, num_results FROM dir_indexterm_{0} WHERE keyword IS {1}'.format(language, keyword['keyword']))
                count = cursor2.fetchall()
                print('Language {0} result: {1}'.format(language, count))
                language_results[language] = count
            results = sorted(scores.iteritems(), key=lambda item: item[1], reverse=True)
            print u'Scores for {0}: {1}'.format(keyword, results)
            if( results[0][0] == 'en' ):
                print('Keyword ranks highest for English. Skipping prompt.')
                continue
            input = raw_input(u'Tag {0} as: [q]uit/[s]kip/[del]ete/[xx] tag as lang]? '.format(keyword))
            input = input.lower()
            if input == 'q':
                exit()
            elif input == 's':
                continue
            elif input == 'del':
                cursor.execute("DELETE FROM dir_indexterm WHERE keywords = '{0}'".format(keyword))
                delresult = cursor.fetchall()
                print('Delete result: {0}'.format(delresult))
            else:
                if input in language_list:
                    model = GetIndexModelFromLanguage(input)
                    if model:
                        dom = model.objects.delete(keywords=keyword)
                else:
                    print '{0} is not a valid language. Skipping'.format(input)
                    continue
