# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import connection
from dir.utils import GetIndexModelFromLanguage
import os
import sys
import json
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def IndexToJson(index, language):
    data = {}
    data['language'] = language
    data['keywords'] = index.keywords
    data['date_indexed'] = index.date_indexed
    data['page_rankings'] = index.page_rankings
    data['num_results'] = index.num_results
    data['num_pages'] = index.num_pages
    data['index_time'] = index.index_time
    data['search_results'] = index.search_results
    data['actively_blocked'] = index.actively_blocked
    data['refused'] = index.refused
    data['typo_for'] = index.typo_for
    data['is_language'] = index.is_language
    data['term_weight'] = index.term_weight
    if language == 'en':
        data['show_ad'] = index.show_ad
        data['verified_english'] = index.verified_english
    return data


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        processed = 0
        added = 0
        index_model = GetIndexModelFromLanguage('sw')
        for index in index_model.objects.all():
            es.index(index='keywords_sw', doc_type='keyword', body=IndexToJson(index, 'sw'))
            processed += 1
            added += 1
            if processed % 1000 == 0:
                print(processed)
        print('Processed {0} index terms and added {1} to elasticsearch'.format(processed, added))
