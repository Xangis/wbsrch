# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import DomainInfo
from dir.utils import *
import csv


def LoadDomainInfoFile(filename):
    processed = 0
    added = 0
    updated = 0
    shouldcrawl = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # id,url,notes,language_association,rank_adjustment,rank_reason,alexa_rank,alexa_rank_date,uses_language_subdirs,max_urls,is_unblockable,uses_language_query_parameter
        # 2,rome.craigslist.it,"",it,0,,,,f,,f,f
        # 1607696,ja-facebook.com,,,0,,288598,2014-03-24,f,,f,f
        first = True
        for row in reader:
            if first:
                first = False
                continue
            processed += 1
            if len(row) >= 5:
                # print(row)
                domain = row[1].strip()
                notes = row[2].strip()
                language_association = row[3].strip()
                subdirs = row[8].strip()
                if subdirs == 'f':
                    uses_language_subdirs = False
                else:
                    uses_language_subdirs = True
                unblockable = row[10].strip()
                if unblockable == 'f':
                    is_unblockable = False
                else:
                    is_unblockable = True
                queryparam = row[11].strip()
                if queryparam == 'f':
                    uses_language_query_parameter = False
                else:
                    uses_language_query_parameter = True
                try:
                    info = DomainInfo.objects.get(url=domain)
                    changed = False
                    move_sites = False
                    if language_association and (info.language_association != language_association):
                        print('Changing {0} language association from {1} to {2}'.format(info.url, info.language_association, language_association))
                        info.language_association = language_association
                        move_sites = True
                        updated += 1
                        changed = True
                    if uses_language_subdirs and (info.uses_language_subdirs != uses_language_subdirs):
                        print('Changing {0} uses_language_subdirs from {1} to {2}'.format(info.url, info.uses_language_subdirs, uses_language_subdirs))
                        print('TODO: Process existing domains')
                        info.uses_language_subdirs = uses_language_subdirs
                        updated += 1
                        changed = True
                    if notes and (info.notes != notes):
                        print('Changing {0} notes from {1} to {2}'.format(info.url, info.notes, notes))
                        info.notes = notes
                        updated += 1
                        changed = True
                    if is_unblockable and (info.is_unblockable != is_unblockable):
                        print('Changing {0} is_unblockable from {1} to {2}'.format(info.url, info.is_unblockable, is_unblockable))
                        info.is_unblockable = is_unblockable
                        updated += 1
                        changed = True
                    if uses_language_query_parameter and (info.uses_language_query_parameter != uses_language_query_parameter):
                        print('Changing {0} uses_language_query_parameter from {1} to {2}'.format(info.url, info.uses_language_query_parameter, uses_language_query_parameter))
                        info.uses_language_query_parameter = uses_language_query_parameter
                        updated += 1
                        changed = True
                    if changed:
                        info.save()
                    if move_sites:
                        pages = SiteInfo.objects.filter(rooturl=domain)
                        print('Moving {0} pages to {1} index'.format(pages.count(), language_association))
                        for page in pages:
                            MoveSiteTo(page, language_association, True, verbose=True)
                except ObjectDoesNotExist:
                    print('Adding new DomainInfo entry for {0} (lang = {1}, notes = {2}, subdirs = {3}, unblockable = {4}, queryparam = {5}).'.format(
                        domain, language_association, notes, uses_language_subdirs, is_unblockable, uses_language_query_parameter))
                    info = DomainInfo()
                    info.url = domain
                    if language_association:
                        info.language_association = language_association
                    if notes:
                        info.notes = notes
                    if uses_language_subdirs:
                        info.uses_language_subdirs = uses_language_subdirs
                    if is_unblockable:
                        info.is_unblockable = is_unblockable
                    if uses_language_query_parameter:
                        info.uses_language_query_parameter = uses_language_query_parameter
                    info.save()
                    added += 1
                    shouldcrawl.append(domain)
        if processed % 10000 == 0:
            print(processed)
        for dom in shouldcrawl:
            print('CRAWL: {0}'.format(dom))
    print('Processed {0} domain infos. {1} were newly added and {2} pieces of information were updated.'.format(processed, added, updated))


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        LoadDomainInfoFile('domain_info.csv')
