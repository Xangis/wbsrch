# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteInfo_fr'
        db.create_table(u'dir_siteinfo_fr', (
            (u'siteinfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.SiteInfo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_fr'])

        # Adding model 'PendingIndex_de'
        db.create_table(u'dir_pendingindex_de', (
            (u'pendingindex_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.PendingIndex'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_de'])

        # Adding model 'SiteInfo_es'
        db.create_table(u'dir_siteinfo_es', (
            (u'siteinfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.SiteInfo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_es'])

        # Adding model 'IndexTerm_fr'
        db.create_table(u'dir_indexterm_fr', (
            (u'indexterm_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.IndexTerm'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_fr'])

        # Adding model 'PendingIndex_fr'
        db.create_table(u'dir_pendingindex_fr', (
            (u'pendingindex_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.PendingIndex'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_fr'])

        # Adding model 'IndexTerm_de'
        db.create_table(u'dir_indexterm_de', (
            (u'indexterm_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.IndexTerm'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_de'])

        # Adding model 'PendingIndex_es'
        db.create_table(u'dir_pendingindex_es', (
            (u'pendingindex_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.PendingIndex'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_es'])

        # Adding model 'IndexTerm_es'
        db.create_table(u'dir_indexterm_es', (
            (u'indexterm_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.IndexTerm'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_es'])

        # Adding model 'SiteInfo_de'
        db.create_table(u'dir_siteinfo_de', (
            (u'siteinfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dir.SiteInfo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_de'])


    def backwards(self, orm):
        # Deleting model 'SiteInfo_fr'
        db.delete_table(u'dir_siteinfo_fr')

        # Deleting model 'PendingIndex_de'
        db.delete_table(u'dir_pendingindex_de')

        # Deleting model 'SiteInfo_es'
        db.delete_table(u'dir_siteinfo_es')

        # Deleting model 'IndexTerm_fr'
        db.delete_table(u'dir_indexterm_fr')

        # Deleting model 'PendingIndex_fr'
        db.delete_table(u'dir_pendingindex_fr')

        # Deleting model 'IndexTerm_de'
        db.delete_table(u'dir_indexterm_de')

        # Deleting model 'PendingIndex_es'
        db.delete_table(u'dir_pendingindex_es')

        # Deleting model 'IndexTerm_es'
        db.delete_table(u'dir_indexterm_es')

        # Deleting model 'SiteInfo_de'
        db.delete_table(u'dir_siteinfo_de')


    models = {
        u'dir.domaininfo': {
            'Meta': {'object_name': 'DomainInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'dir.excludedsite': {
            'Meta': {'object_name': 'ExcludedSite', 'db_table': "u'excluded_site'"},
            'detailedreason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.feedbackitem': {
            'Meta': {'object_name': 'FeedbackItem'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'num_search_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.indexterm': {
            'Meta': {'object_name': 'IndexTerm'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de', '_ormbases': [u'dir.IndexTerm']},
            u'indexterm_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.IndexTerm']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es', '_ormbases': [u'dir.IndexTerm']},
            u'indexterm_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.IndexTerm']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr', '_ormbases': [u'dir.IndexTerm']},
            u'indexterm_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.IndexTerm']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.pendingindex': {
            'Meta': {'object_name': 'PendingIndex'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_de': {
            'Meta': {'object_name': 'PendingIndex_de', '_ormbases': [u'dir.PendingIndex']},
            u'pendingindex_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.PendingIndex']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.pendingindex_es': {
            'Meta': {'object_name': 'PendingIndex_es', '_ormbases': [u'dir.PendingIndex']},
            u'pendingindex_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.PendingIndex']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.pendingindex_fr': {
            'Meta': {'object_name': 'PendingIndex_fr', '_ormbases': [u'dir.PendingIndex']},
            u'pendingindex_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.PendingIndex']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.pendingurl': {
            'Meta': {'object_name': 'PendingUrl'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'dir.searchlog': {
            'Meta': {'object_name': 'SearchLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {})
        },
        u'dir.siteinfo': {
            'Meta': {'object_name': 'SiteInfo', 'db_table': "u'site_info'"},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_de': {
            'Meta': {'object_name': 'SiteInfo_de', '_ormbases': [u'dir.SiteInfo']},
            u'siteinfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.SiteInfo']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.siteinfo_es': {
            'Meta': {'object_name': 'SiteInfo_es', '_ormbases': [u'dir.SiteInfo']},
            u'siteinfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.SiteInfo']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dir.siteinfo_fr': {
            'Meta': {'object_name': 'SiteInfo_fr', '_ormbases': [u'dir.SiteInfo']},
            u'siteinfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dir.SiteInfo']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dir']