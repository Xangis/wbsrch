# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PendingIndex_sk'
        db.create_table(u'dir_pendingindex_sk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_sk'])

        # Adding model 'SiteInfo_sk'
        db.create_table(u'dir_siteinfo_sk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.TextField')(unique=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_sk'])

        # Adding model 'SearchLog_sk'
        db.create_table(u'dir_searchlog_sk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('search_count', self.gf('django.db.models.fields.IntegerField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_sk'])

        # Adding model 'IndexTerm_sk'
        db.create_table(u'dir_indexterm_sk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_sk'])


    def backwards(self, orm):
        # Deleting model 'PendingIndex_sk'
        db.delete_table(u'dir_pendingindex_sk')

        # Deleting model 'SiteInfo_sk'
        db.delete_table(u'dir_siteinfo_sk')

        # Deleting model 'SearchLog_sk'
        db.delete_table(u'dir_searchlog_sk')

        # Deleting model 'IndexTerm_sk'
        db.delete_table(u'dir_indexterm_sk')


    models = {
        u'dir.domaininfo': {
            'Meta': {'object_name': 'DomainInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_association': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_cs': {
            'Meta': {'object_name': 'IndexTerm_cs'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_da': {
            'Meta': {'object_name': 'IndexTerm_da'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_el': {
            'Meta': {'object_name': 'IndexTerm_el'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fi': {
            'Meta': {'object_name': 'IndexTerm_fi'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_hr': {
            'Meta': {'object_name': 'IndexTerm_hr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_hu': {
            'Meta': {'object_name': 'IndexTerm_hu'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_is': {
            'Meta': {'object_name': 'IndexTerm_is'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_it': {
            'Meta': {'object_name': 'IndexTerm_it'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_lt': {
            'Meta': {'object_name': 'IndexTerm_lt'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_lv': {
            'Meta': {'object_name': 'IndexTerm_lv'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_nl': {
            'Meta': {'object_name': 'IndexTerm_nl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_no': {
            'Meta': {'object_name': 'IndexTerm_no'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pl': {
            'Meta': {'object_name': 'IndexTerm_pl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pt': {
            'Meta': {'object_name': 'IndexTerm_pt'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_ro': {
            'Meta': {'object_name': 'IndexTerm_ro'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sk': {
            'Meta': {'object_name': 'IndexTerm_sk'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sv': {
            'Meta': {'object_name': 'IndexTerm_sv'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sw': {
            'Meta': {'object_name': 'IndexTerm_sw'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_tr': {
            'Meta': {'object_name': 'IndexTerm_tr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.pendingindex': {
            'Meta': {'object_name': 'PendingIndex'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_cs': {
            'Meta': {'object_name': 'PendingIndex_cs'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_da': {
            'Meta': {'object_name': 'PendingIndex_da'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_de': {
            'Meta': {'object_name': 'PendingIndex_de'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_el': {
            'Meta': {'object_name': 'PendingIndex_el'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_es': {
            'Meta': {'object_name': 'PendingIndex_es'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_fi': {
            'Meta': {'object_name': 'PendingIndex_fi'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_fr': {
            'Meta': {'object_name': 'PendingIndex_fr'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_hr': {
            'Meta': {'object_name': 'PendingIndex_hr'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_hu': {
            'Meta': {'object_name': 'PendingIndex_hu'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_is': {
            'Meta': {'object_name': 'PendingIndex_is'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_it': {
            'Meta': {'object_name': 'PendingIndex_it'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_lt': {
            'Meta': {'object_name': 'PendingIndex_lt'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_lv': {
            'Meta': {'object_name': 'PendingIndex_lv'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_nl': {
            'Meta': {'object_name': 'PendingIndex_nl'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_no': {
            'Meta': {'object_name': 'PendingIndex_no'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_pl': {
            'Meta': {'object_name': 'PendingIndex_pl'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_pt': {
            'Meta': {'object_name': 'PendingIndex_pt'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ro': {
            'Meta': {'object_name': 'PendingIndex_ro'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_sk': {
            'Meta': {'object_name': 'PendingIndex_sk'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_sv': {
            'Meta': {'object_name': 'PendingIndex_sv'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_sw': {
            'Meta': {'object_name': 'PendingIndex_sw'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_tr': {
            'Meta': {'object_name': 'PendingIndex_tr'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
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
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_cs': {
            'Meta': {'object_name': 'SearchLog_cs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_da': {
            'Meta': {'object_name': 'SearchLog_da'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_de': {
            'Meta': {'object_name': 'SearchLog_de'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_el': {
            'Meta': {'object_name': 'SearchLog_el'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_es': {
            'Meta': {'object_name': 'SearchLog_es'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fi': {
            'Meta': {'object_name': 'SearchLog_fi'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fr': {
            'Meta': {'object_name': 'SearchLog_fr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hr': {
            'Meta': {'object_name': 'SearchLog_hr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hu': {
            'Meta': {'object_name': 'SearchLog_hu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_is': {
            'Meta': {'object_name': 'SearchLog_is'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_it': {
            'Meta': {'object_name': 'SearchLog_it'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lt': {
            'Meta': {'object_name': 'SearchLog_lt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lv': {
            'Meta': {'object_name': 'SearchLog_lv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nl': {
            'Meta': {'object_name': 'SearchLog_nl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_no': {
            'Meta': {'object_name': 'SearchLog_no'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pl': {
            'Meta': {'object_name': 'SearchLog_pl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pt': {
            'Meta': {'object_name': 'SearchLog_pt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ro': {
            'Meta': {'object_name': 'SearchLog_ro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sk': {
            'Meta': {'object_name': 'SearchLog_sk'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sv': {
            'Meta': {'object_name': 'SearchLog_sv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sw': {
            'Meta': {'object_name': 'SearchLog_sw'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_tr': {
            'Meta': {'object_name': 'SearchLog_tr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
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
        u'dir.siteinfo_cs': {
            'Meta': {'object_name': 'SiteInfo_cs'},
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
        u'dir.siteinfo_da': {
            'Meta': {'object_name': 'SiteInfo_da'},
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
            'Meta': {'object_name': 'SiteInfo_de'},
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
        u'dir.siteinfo_el': {
            'Meta': {'object_name': 'SiteInfo_el'},
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
        u'dir.siteinfo_es': {
            'Meta': {'object_name': 'SiteInfo_es'},
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
        u'dir.siteinfo_fi': {
            'Meta': {'object_name': 'SiteInfo_fi'},
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
        u'dir.siteinfo_fr': {
            'Meta': {'object_name': 'SiteInfo_fr'},
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
        u'dir.siteinfo_hr': {
            'Meta': {'object_name': 'SiteInfo_hr'},
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
        u'dir.siteinfo_hu': {
            'Meta': {'object_name': 'SiteInfo_hu'},
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
        u'dir.siteinfo_is': {
            'Meta': {'object_name': 'SiteInfo_is'},
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
        u'dir.siteinfo_it': {
            'Meta': {'object_name': 'SiteInfo_it'},
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
        u'dir.siteinfo_lt': {
            'Meta': {'object_name': 'SiteInfo_lt'},
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
        u'dir.siteinfo_lv': {
            'Meta': {'object_name': 'SiteInfo_lv'},
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
        u'dir.siteinfo_nl': {
            'Meta': {'object_name': 'SiteInfo_nl'},
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
        u'dir.siteinfo_no': {
            'Meta': {'object_name': 'SiteInfo_no'},
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
        u'dir.siteinfo_pl': {
            'Meta': {'object_name': 'SiteInfo_pl'},
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
        u'dir.siteinfo_pt': {
            'Meta': {'object_name': 'SiteInfo_pt'},
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
        u'dir.siteinfo_ro': {
            'Meta': {'object_name': 'SiteInfo_ro'},
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
        u'dir.siteinfo_sk': {
            'Meta': {'object_name': 'SiteInfo_sk'},
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
        u'dir.siteinfo_sv': {
            'Meta': {'object_name': 'SiteInfo_sv'},
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
        u'dir.siteinfo_sw': {
            'Meta': {'object_name': 'SiteInfo_sw'},
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
        u'dir.siteinfo_tr': {
            'Meta': {'object_name': 'SiteInfo_tr'},
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
        }
    }

    complete_apps = ['dir']