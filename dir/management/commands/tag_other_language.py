# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import IndexTerm, language_list
from dir.utils import GetIndexModelFromLanguage, GetSiteInfoModelFromLanguage
import sys


class Command(BaseCommand):
    help = """
    This gets the words from the English index and checks them against the index for another language. If
    there are more than X (threshold) results, it prompts you whether to tag that word as being in the target
    language. Works based on the idea that if a word shows up a lot in a known-other-language, that word might
    be in that language.
    """
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default=None, action='store', tydest='language', help='Language to use for pending indexes (required).')
        parser.add_argument('-b', '--bruteforce', default=False, action='store_true', dest='bruteforce', help='Brute force mode, overrides language, wordlength, and threshold. (default=No)')
        parser.add_argument('-m', '--maxwords', default=100000, action='store', type=int, dest='maxwords', help='Max number of terms to index. (default=1000000)')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Offset from start of list. (default=0)')
        parser.add_argument('-w', '--wordlength', default=3, action='store', type=int, dest='wordlength', help='Min word length to check. (default=3)')
        parser.add_argument('-t', '--threshold', default=100, action='store', type=int, dest='threshold', help='Min number of results to suggest tag. (default=100)')

    def handle(self, *args, **options):
        maxwords = options.get('maxwords', 0)
        language = options.get('language', None)
        threshold = options.get('threshold', None)
        wordlength = options.get('wordlength', 1)
        offset = options.get('offset', 0)
        bruteforce = options.get('bruteforce', False)
        notfound = 0
        numfound = 0
        alreadytagged = 0
        ignored = 0
        verifiedenglish = 0
        newenglish = 0
        if bruteforce:
            term_model = GetIndexModelFromLanguage('en')
            language = 'en'
            language_counts = {}
            for lang in language_list:
                tmpmodel = GetSiteInfoModelFromLanguage(lang)
                language_counts[lang] = float(tmpmodel.objects.all().count())
            print('Language Page Counts: {0}'.format(language_counts))
            queryset = term_model.objects.filter(is_language__isnull=True, verified_english=False, typo_for__isnull=True).order_by('id')[offset:offset + maxwords]
        else:
            term_model = GetIndexModelFromLanguage(language)
            if not language:
                print('Language is required.')
                return
            queryset = term_model.objects.all()[offset:offset + maxwords]
        print('Tagging other languages with {0} max words and language {1}.'.format(maxwords, language))
        numdone = 0
        for item in queryset:
            numdone = numdone + 1
            if not bruteforce:
                if len(item.keywords) < wordlength:
                    ignored = ignored + 1
                    continue
                if item.num_results < threshold:
                    continue
                try:
                    term = IndexTerm.objects.get(keywords=item.keywords)
                    if term.is_language:
                        alreadytagged = alreadytagged + 1
                        continue
                    if term.verified_english:
                        verifiedenglish = verifiedenglish + 1
                        continue
                except ObjectDoesNotExist:
                    notfound = notfound + 1
                    continue
                numfound = numfound + 1
                prompt = u'[{5}] Tag {0} as {1} ({2} results in english, {3} in {1}) updated {4}: [y]es/[n]o/[e]nglishword/[q]uit? '.format(
                    term.keywords, language, term.num_results, item.num_results, term.date_indexed, numdone + offset)
                rinput = input(prompt.encode(sys.stdout.encoding)).lower()
                if rinput == 'y':
                    term.is_language = language
                    term.save(keep_date=True)
                if rinput == 'e':
                    term.verified_english = True
                    verifiedenglish = verifiedenglish + 1
                    newenglish = newenglish + 1
                    term.save(keep_date=True)
                if rinput == 'q':
                    break
            else:
                if item.is_language:
                    alreadytagged = alreadytagged + 1
                    continue
                if item.verified_english:
                    verifiedenglish = verifiedenglish + 1
                    continue
                percents = {}
                for lang in language_list:
                    tmpmodel = GetIndexModelFromLanguage(lang)
                    try:
                        term = tmpmodel.objects.get(keywords=item.keywords)
                        percents[lang] = (term.num_results * 100.0) / language_counts[lang]
                    except ObjectDoesNotExist:
                        continue
                results = sorted(percents.iteritems(), key=lambda x: x[1], reverse=True)
                print('Results for [{0}] {1} ({2} in English):'.format(item.id, item.keywords, item.num_results))
                resultstr = ''
                for rval in results:
                    resultstr += '{0} = {1:.2f}%, '.format(rval[0], rval[1])
                print(resultstr)
                prompt = u'Enter the two-letter language to tag as, or e for english, q to quit, anything else to skip: '
                rinput = input(prompt.encode(sys.stdout.encoding)).lower()
                if rinput == 'e' or rinput == 'en':
                    print('{0} tagged as English.'.format(item.keywords))
                    item.verified_english = True
                    item.is_language = None
                    verifiedenglish = verifiedenglish + 1
                    newenglish = newenglish + 1
                    item.save(keep_date=True)
                elif rinput in language_list:
                    print('{0} tagged as {1}'.format(item.keywords, rinput))
                    item.is_language = rinput
                    item.save(keep_date=True)
                elif rinput == 'q':
                    break
                else:
                    print('Skipping ({0})'.format(rinput))
        print('Processed {0} words and {1} were not found, {2} hit the threshold of {3}, and {4} were already tagged, {5} ignored short words, {6} verified English ({7} newly so).'.format(
            numdone, notfound, numfound, threshold, alreadytagged, ignored, verifiedenglish, newenglish))
