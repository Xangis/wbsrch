# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from pprint import pprint
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-i', '--index', default=False, action='store_true', dest='index', help='Search the index rather than pages (default=False).')
        parser.add_argument('-k', '--keywords', action='store', dest='keywords', help='Keyword to search for.')
        parser.add_argument('-a', '--all', default=False, action='store_true', dest='all', help='Query ALL documents (limit 20, default=False).')

    def handle(self, *args, **options):
        keywords = options.get('keywords', 'habari')
        index = options.get('index', False)
        all = options.get('all', False)
        # es.index(index='pages', doc_type='page', id=page.url, body=SiteInfoToJson(page, 'sw'))
        # results = es.search(index='pages', body={"query": {"match": {"pagetext": "habari"}}})
        # results = es.search(index='pages', body={"query": {"match_all": {"pagetext": "habari"}}})
        print('Keywords: {0}, Index: {1}, All: {2}'.format(keywords, index, all))
        if index:
            if all:
                # results = es.search(index='keywords_sw', size=20, body={"query": {"term": {"pagetext.raw": keywords}}})
                query = {"query": {"match_all": {}}}
            else:
                # query = {"query": {"term": {"pagetext": keywords}}}
                query = {"query": {"multi_match": {"query": keywords, 'fields': ['keywords']}}}
        else:
            if all:
                query = {"query": {"match_all": {}}}
            else:
                query = {"query": {"multi_match": {"query": keywords, 'fields': ['title^3', 'description^0.5', 'text', 'domain^1.5', 'firstheadtag^4', 'firsth2tag^2', 'firsth3tag^1.2', 'image_alt_tags^0.25', 'keywords^0.1', 'url^0.8', 'image_title_tags^0.2']}}}
                # results = es.search(index='pages', size=20, body={"query": {"term": {"keywords.raw": keywords}}})
        print('Query:\n{0}'.format(query))
        if index:
            results = es.search(index='keywords_sw', size=20, body=query)
        else:
            results = es.search(index='pages', size=20, body=query)
        print("Got %d Hits:" % results['hits']['total']['value'])
        print("[hits][hits] length: {0}".format(len(results['hits']['hits'])))
        for res in results['hits']['hits']:
            result = res['_source']
            score = res['_score']
            if index:
                result = res
                print('Score: {0}'.format(score))
                pprint(result)
            else:
                print('Score: {0}'.format(score))
                # pprint(result)
                pprint(result['title'])
                desc = result['description']
                if desc:
                    pprint(result['description'])
                else:
                    pprint('TEXT: ' + result['text'][0:250])
                pprint(result['url'])
                print(' ')
