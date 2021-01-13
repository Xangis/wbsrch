# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import language_list
from dir.utils import GetIndexModelFromLanguage


class Command(BaseCommand):
    help = """
    This gets the words from the English index and checks them against the index for another language. If
    there are more than X (threshold) results, it prompts you whether to tag that word as being in the target
    language. Works based on the idea that if a word shows up a lot in a known-other-language, that word might
    be in that language.
    """
    def add_arguments(self, parser):
        parser.add_argument('-s', '--startafter', default=None, action='store', dest='startafter', help='Start after <string>. Only useful for resuming an afterz or beforezero categorize.')
        parser.add_argument('-l', '--language', default='en', action='store', dest='language', help='Language to use for index keywords (default=en).')
        parser.add_argument('-w', '--wordlength', default=3, action='store', type=int, dest='wordlength', help='Min word length to check. (default=3)')
        parser.add_argument('-t', '--threshold', default=100, action='store', type=int, dest='threshold', help='Min number of results to suggest tag. (default=100)')

    def handle(self, *args, **options):
        startafter = options.get('startafter', None)
        wordlength = options.get('wordlength', None)
        threshold = options.get('threshold', None)
        index_language = options.get('language', 'en')
        language_checked = GetIndexModelFromLanguage(index_language)
        if startafter:
            keywords = language_checked.objects.filter(keywords__gt=startafter, is_language=None).values_list('keywords', flat=True).order_by('keywords')
        else:
            keywords = language_checked.objects.filter(is_language=None).values_list('keywords', flat=True).order_by('keywords')
        tooshort = 0
        toofew = 0
        notprompted = 0
        for keyword in keywords:
            if len(keyword) < wordlength:
                tooshort = tooshort + 1
                continue
            langcounts = {}
            for language in language_list:
                model = GetIndexModelFromLanguage(language)
                try:
                    kw = model.objects.get(keywords=keyword)
                    if kw is not None and (kw.num_pages > 0):
                        langcounts[language] = kw.num_pages
                    elif kw.num_results > 0:
                        langcounts[language] = kw.num_results
                except ObjectDoesNotExist:
                    continue
            scores = sorted(langcounts.iteritems(), key=lambda item: item[1], reverse=True)
            if len(scores) < 1:
                continue
            print('Scores for "{0}": {1}'.format(keyword, scores))
            if scores[0][0] == 'en':
                notprompted = notprompted + 1
                continue
            if threshold and (scores[0][1] < threshold):
                toofew = toofew + 1
                continue
            rinput = input('Tag {0} as: [q]uit/[s]kip/[xx] tag as lang]? '.format(keyword))
            rinput = rinput.lower()
            if rinput == 'q':
                exit()
            elif rinput == 's':
                continue
            else:
                if rinput in language_list:
                    kw = language_checked.objects.get(keywords=keyword)
                    kw.is_language = rinput
                    kw.save()
                    print('Setting keyword "{0}" as language {1}'.format(keyword, rinput))
        print('Done. {0} too-short and {1} below-threshold words were skipped, and {2} had more English results.'.format(tooshort, toofew, notprompted))
