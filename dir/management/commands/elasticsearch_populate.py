# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import connection
from dir.utils import GetSiteInfoModelFromLanguage
import os
import sys
import json
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def SiteInfoToJson(page, language):
    data = {}
    data['language'] = language
    data['domain'] = page.rooturl
    data['tld'] = page.rooturl.split('.')[-1]
    data['url'] = page.url
    data['title'] = page.pagetitle
    data['description'] = page.pagedescription
    data['firstheadtag'] = page.pagefirstheadtag
    data['firsth2tag'] = page.pagefirsth2tag
    data['firsth3tag'] = page.pagefirsth3tag
    data['keywords'] = page.pagekeywords
    data['contents'] = page.pagecontents
    data['text'] = page.pagetext
    data['page_size'] = page.pagesize
    data['last_crawled'] = page.lastcrawled
    data['first_crawled'] = page.firstcrawled
    data['ip'] = page.ip
    data['num_errors'] = page.num_errors
    data['server_header'] = page.server_header
    data['content_type_header'] = page.content_type_header
    data['num_css_files'] = page.num_css_files
    data['num_images'] = page.num_images
    data['num_javascripts'] = page.num_javascripts
    data['num_iframes'] = page.num_iframes
    data['num_audio_tags'] = page.num_audio_tags
    data['num_video_tags'] = page.num_video_tags
    data['num_svg_tags'] = page.num_svg_tags
    data['num_canvas_tags'] = page.num_canvas_tags
    data['image_alt_tags'] = page.image_alt_tags
    data['image_title_tags'] = page.image_title_tags
    data['image_filenames'] = page.image_filenames
    data['simhash_value'] = page.simhash_value
    return data


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        processed = 0
        added = 0
        site_model = GetSiteInfoModelFromLanguage('sw')
        for page in site_model.objects.all():
            es.index(index='pages', doc_type='page', id=page.url, body=SiteInfoToJson(page, 'sw'))
            processed += 1
            added += 1
        print('Processed {0} pages and added {1} to elasticsearch'.format(processed, added))
