# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DomainInfo'
        db.create_table(u'dir_domaininfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['DomainInfo'])


    def backwards(self, orm):
        # Deleting model 'DomainInfo'
        db.delete_table(u'dir_domaininfo')


    models = {
        u'dir.domaininfo': {
            'Meta': {'object_name': 'DomainInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
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
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dir']