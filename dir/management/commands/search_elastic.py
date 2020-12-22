# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import connection
from dir.utils import GetSiteInfoModelFromLanguage
import os
import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        processed = 0
        added = 0
        # es.index(index='pages', doc_type='page', id=page.url, body=SiteInfoToJson(page, 'sw'))
        # results = es.search(index='pages', body={"query": {"match": {"pagetext": "habari"}}})
        # results = es.search(index='pages', body={"query": {"match_all": {"pagetext": "habari"}}})
        results = es.search(index='pages', size=20, body={"query": {"match_all": {}}})
        print("Got %d Hits:" % results['hits']['total']['value'])
        print("[hits][hits] length: {0}".format(len(results['hits']['hits'])))
        for res in results['hits']['hits']:
             result = res['_source']
             #pprint(result)
             pprint(result['title'])
             pprint(result['description'])
             pprint(result['url'])
             print(' ')
