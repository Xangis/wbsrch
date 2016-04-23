# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import PendingIndex, IndexTerm, DomainInfo
from dir.utils import AddPendingTerm, GetIndexModelFromLanguage, GetRootUrl
import codecs

class Command(BaseCommand):
    help = """
    This command processes a file containing a list of words. If those words are not already indexed for the specified
    language, it adds them to the pending index list so that the indexer will build an index term for them.
    """
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        make_option('-d', '--domains', default=False, action='store_true', dest='domains', help='Process file as a domain list and print the domains that need to be crawled. (default=no).'),
        make_option('-p', '--print', default=False, action='store_true', dest='print', help='Just print the terms that are not indexed to the screen, do not create pending terms. (default=no).'),
        make_option('-n', '--noindividual', default=False, action='store_true', dest='noindividual', help='Make sure individual words of a phrase are not indexed (default=False)'),
        make_option('-m', '--maxwords', default=5, action='store', type='int', dest='maxwords', help='Max number of terms to index. (default=5)'),
        make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),
    )

    def handle(self, *args, **options):
        filename = options.get('file', None)
        maxwords = options.get('maxwords', 0)
        language = options.get('language', 'en')
        domains = options.get('domains', False)
        printem = options.get('print', False)
        noindividual = options.get('noindividual', None)
        term_model = GetIndexModelFromLanguage(language)
        print 'Using file {0} with {1} max words and language {2}.'.format(filename, maxwords, language)
        f = open(filename, 'rb')
        reader = codecs.getreader('utf8')(f)
        numdone = 0
        numadded = 0
        for line in reader:
             line = GetRootUrl(line.strip().lower())
             # Do not queue anything less than 2 characters long.
             if len(line) < 2:
                 continue
             try:
                 if domains:
                     info = DomainInfo.objects.get(url=line)
                 else:
                     term = term_model.objects.get(keywords=line)
             except ObjectDoesNotExist:
                 if domains or printem:
                     try:
                         print u'{0}'.format(line)
                         numadded = numadded + 1
                     except:
                         pass
                 else:
                     AddPendingTerm(line, language, 'add_new_to_pending from file {0}'.format(filename))
                     print u'Added {0}.'.format(line)
                     numadded = numadded + 1
             if not noindividual and not domains:
                 if ' ' in line:
                     words = line.split(' ')
                     for word in words: 
                         try:
                             term = term_model.objects.get(keywords=word)
                         except ObjectDoesNotExist:
                             if not printem:
                                 try:
                                     AddPendingTerm(word, language, 'add_new_to_pending from file {0}'.format(filename))
                                 except:
                                     pass
                             try:
                                 print u'{0}.'.format(word)
                             except:
                                 pass
                             numadded = numadded + 1
             numdone = numdone + 1
             if numdone >= maxwords:
                  break
        if domains:
            print 'Processed {0} lines and {1} domains need to be crawled.'.format(numdone, numadded, language)
        else:
            print 'Processed {0} words and added {1} to the pending {2} index.'.format(numdone, numadded, language)
