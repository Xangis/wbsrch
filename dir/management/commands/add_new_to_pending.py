# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import DomainInfo
from dir.utils import AddPendingTerm, GetIndexModelFromLanguage, GetRootUrl, CleanSearchText
import codecs


class Command(BaseCommand):
    help = """
    This command processes a file containing a list of words. If those words are not already indexed for the specified
    language, it adds them to the pending index list so that the indexer will build an index term for them.
    """

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default='en', action='store', dest='language', help='Language to use for pending indexes (default=en).')
        parser.add_argument('-d', '--domains', default=False, action='store_true', dest='domains', help='Process file as a domain list and print the domains that need to be crawled. Redundant with -p since it only prints (default=no).')
        parser.add_argument('-p', '--print', default=False, action='store_true', dest='print', help='Just print the terms that are not indexed to the screen, do not create pending terms. (default=no).')
        parser.add_argument('-n', '--noindividual', default=False, action='store_true', dest='noindividual', help='Make sure individual words of a phrase are not indexed (default=False)')
        parser.add_argument('-m', '--maxwords', default=100000000, action='store', type=int, dest='maxwords', help='Max number of terms to index. (default=100000000)')
        parser.add_argument('-f', '--file', default=None, action='store', dest='file', help='Load term list from specified file.')

    def handle(self, *args, **options):
        filename = options.get('file', None)
        maxwords = options.get('maxwords', 0)
        language = options.get('language', 'en')
        domains = options.get('domains', False)
        printem = options.get('print', False)
        noindividual = options.get('noindividual', None)
        term_model = GetIndexModelFromLanguage(language)
        if domains and not filename:
            print('Filename is a required argument when processing domains.')
            return False
        print('Using file {0} with {1} max words and language {2}.'.format(filename, maxwords, language))
        f = open(filename, 'rb')
        reader = codecs.getreader('utf8')(f)
        numdone = 0
        numadded = 0
        numlines = 1
        try:
            for line in reader:
                numlines = numlines + 1
                # Don't consider full URLs as valid search terms from file, instead use the root URL, if possible.
                try:
                    line = GetRootUrl(line.strip().lower())
                except Exception:
                    line = CleanSearchText(line.strip().lower())
                # Do not queue anything less than 2 characters long.
                if len(line) < 2:
                    continue
                try:
                    if domains:
                        DomainInfo.objects.get(url=line)
                    else:
                        term_model.objects.get(keywords=line)
                except ObjectDoesNotExist:
                    if domains or printem:
                        try:
                            print('{0}'.format(line))
                            numadded = numadded + 1
                        except Exception:
                            pass
                    else:
                        if AddPendingTerm(line, language, 'add_new_to_pending from file {0}'.format(filename), priority=2):
                            print('Added {0}.'.format(line))
                        numadded = numadded + 1
                if not noindividual and not domains:
                    if ' ' in line:
                        words = line.split(' ')
                        for word in words:
                            try:
                                term_model.objects.get(keywords=word)
                            except ObjectDoesNotExist:
                                if not printem:
                                    try:
                                        AddPendingTerm(word, language, 'add_new_to_pending from file {0}'.format(filename), priority=2)
                                    except Exception:
                                        pass
                                try:
                                    print('{0}'.format(word))
                                except Exception:
                                    pass
                                numadded = numadded + 1
                numdone = numdone + 1
                if numdone >= maxwords:
                    break
        except UnicodeDecodeError:
            print('UnicodeDecodeError on line {0}'.format(numlines))
        if domains:
            print('Processed {0} lines and {1} domains need to be crawled.'.format(numdone, numadded))
        else:
            print('Processed {0} words and added {1} to the pending {2} index.'.format(numdone, numadded, language))
