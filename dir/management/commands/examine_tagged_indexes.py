# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import IndexTerm, DomainInfo, BlockedSite
import json
from collections import Counter


class Command(BaseCommand):
    help = """
    Checks all of the index terms tagged as a particular language, counting up the URLs from each domain that are
    in the results for them. It uses this data to generate a score, with high scores meaning that a domain is
    probably in that language, i.e. a score of 900 for DE means that domain is probably in German.
    """
    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', default=None, action='store', dest='language', help='Language to use for pending indexes (required).')
        parser.add_argument('-b', '--blocked', default=False, action='store_true', dest='blocked', help='Analyze blocked domains only. (default=No)')
        parser.add_argument('-r', '--refused', default=False, action='store_true', dest='refused', help='Analyze refused domains only. (default=No)')
        parser.add_argument('-i', '--includeall', default=False, action='store_true', dest='includeall', help='Include all domains, including those tagged as English or other languages. (default=No)')
        # parser.add_argument('-m', '--maxwords', default=100000, action='store', type='int', dest='maxwords', help='Max number of terms to index. (default=1000000)')
        # parser.add_argument('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Offset from start of list. (default=0)')
        # parser.add_argument('-w', '--wordlength', default=3, action='store', type='int', dest='wordlength', help='Min word length to check. (default=3)')
        parser.add_argument('-s', '--shutup', default=False, action='store_true', dest='shutup', help='Be silent about missing domain infos. (default=no)')
        parser.add_argument('-c', '--cutoff', default=None, action='store', type=int, dest='cutoff', help='Max number of hits to show result. (default=no limit)')
        parser.add_argument('-t', '--threshold', default=10, action='store', type=int, dest='threshold', help='Min number of hits to show result. (default=10)')

    def handle(self, *args, **options):
        language = options.get('language', None)
        blocked = options.get('blocked', None)
        refused = options.get('refused', None)
        includeall = options.get('includeall', None)
        threshold = options.get('threshold', None)
        cutoff = options.get('cutoff', None)
        shutup = options.get('shutup', None)
        if not language and not blocked and not refused:
            print('One of language, blocked, or refused is required.')
            return
        if language:
            items = IndexTerm.objects.filter(is_language=language)
        elif refused:
            items = IndexTerm.objects.filter(refused=True)
        elif blocked:
            items = IndexTerm.objects.filter(actively_blocked=True)
        counts = Counter()
        print('Processing {0} index terms.'.format(items.count()))
        for item in items:
            sites = json.loads(item.search_results)
            for site in sites:
                num = len(site[1]['urls'])
                # print "{0} = {1}".format(site[0], num)
                if includeall:
                    counts.update({site[0]: num})
                else:
                    try:
                        blocked = BlockedSite.objects.get(url=site[0])
                        continue
                    except ObjectDoesNotExist:
                        pass
                    try:
                        exists = DomainInfo.objects.get(url=site[0])
                        # Language processing: skip sites already tagged with a language.
                        if language:
                            if not exists.language_association and not exists.uses_language_subdirs and not exists.uses_language_query_parameter and not exists.uses_langid:
                                counts.update({site[0]: num})
                        # Blocked/refused processing: skip sites verified not porn.
                        elif not exists.verified_notporn:
                            counts.update({site[0]: num})
                    except ObjectDoesNotExist:
                        if not shutup:
                            print('Domain {0} not found for term {1}'.format(site[0], item.keywords))
                        counts.update({site[0]: num})
        for item in counts.most_common():
            if threshold and item[1] < threshold:
                break
            if cutoff and item[1] > cutoff:
                continue
            print('{0} {1}  https://wbsrch.com/domain/?q={1}'.format(item[1], item[0]))
