# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SiteInfo.pagedescritpion'
        db.delete_column(u'site_info', 'pagedescritpion')

        # Adding field 'SiteInfo.pagedescription'
        db.add_column(u'site_info', 'pagedescription',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SiteInfo.pagedescritpion'
        db.add_column(u'site_info', 'pagedescritpion',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'SiteInfo.pagedescription'
        db.delete_column(u'site_info', 'pagedescription')


    models = {
        u'dir.excludedsite': {
            'Meta': {'object_name': 'ExcludedSite', 'db_table': "u'excluded_site'"},
            'detailedreason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dir.siteinfo': {
            'Meta': {'object_name': 'SiteInfo', 'db_table': "u'site_info'"},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rooturl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['dir']