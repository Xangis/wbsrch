# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.language import NLTKLanguageDetect, IdentifyPageLanguage, IdentifyLanguage

class Command(BaseCommand):
    help = """Tool for semi-manual or keyword language categorization."""

    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Two-letter lowercase language code to check'),
        make_option('-m', '--maxresults', default=10000000, action='store', type='int', dest='maxresults', help='Max number of keyword results to start with'),
    )

    def handle(self, *args, **options):
        check_language = options['language']
        max_results = options['maxresults']
        result = None
        cursor = connections['indexes'].cursor()
        cursor2 = connections['indexes'].cursor()
        uncategorized_domains = []
        # We start with the domains having the most pages and descend.
        if( check_language == 'en'):
            cursor.execute(u"SELECT keywords, num_results FROM dir_indexterm WHERE (is_language IS NULL or is_language='') AND actively_blocked = false AND (typo_for IS NULL or typo_for='') AND verified_english = false AND num_results <= {0} ORDER BY num_results DESC".format(max_results))
        else:
            cursor.execute(u"SELECT keywords, num_results FROM dir_indexterm_{0} WHERE (is_language IS NULL or is_language='') AND actively_blocked = false AND (typo_for IS NULL or typo_for='') AND num_results <= {1} ORDER BY num_results DESC".format(check_language, max_results))
        keywords = cursor.fetchall()
        for keyword in keywords:
            # Skip words less than 4 letters long.
            if len(keyword[0]) < 4:
                continue
            language_results = {}
            print(u'Checking Keyword: {0}'.format(keyword))
            for language in language_list:
                if language == 'en':
                    cursor2.execute(u"SELECT keywords, num_results FROM dir_indexterm WHERE keywords = '{0}'".format(keyword[0].replace("'", "''")))
                else:
                    cursor2.execute(u"SELECT keywords, num_results FROM dir_indexterm_{0} WHERE keywords = '{1}'".format(language, keyword[0].replace("'", "''")))
                count = cursor2.fetchall()
                #print(u'Language {0} result: {1}'.format(language, count))
                language_results[language] = count
            results = sorted(language_results.iteritems(), key=lambda item: item[1], reverse=True)
            print(u'Scores for {0}: {1}'.format(keyword, results))
            if( results[0][0] == 'en' ):
                print(u'Keyword ranks highest for English. Skipping prompt.')
                continue
            input = raw_input(u'Tag {0} as: [q]uit/[s]kip/[del]ete/[xx] tag as lang]? '.format(keyword))
            input = input.lower()
            if input == 'q':
                exit()
            elif input == 's':
                continue
            elif input == 'del':
                model = GetIndexModelFromLanguage(check_language)
                if model:
                    dom = model.objects.delete(keywords=keyword[0])
            else:
                if input in language_list:
                    model = GetIndexModelFromLanguage(check_language)
                    if model:
                        dom = model.objects.get(keywords=keyword[0])
                        if( input == 'en' and check_language == 'en'):
                            print('Setting keyword as verified_english = True')
                            dom.verified_english = True
                            dom.save()
                        else:
                            print('Setting keyword as language {0}'.format(input))
                            dom.is_language = input
                            dom.save()
                else:
                    print(u'{0} is not a valid language. Skipping'.format(input))
                    continue
