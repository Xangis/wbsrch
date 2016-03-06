# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IndexTerm_sw'
        db.create_table(u'dir_indexterm_sw', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_sw'])

        # Adding model 'PendingIndex_ro'
        db.create_table(u'dir_pendingindex_ro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_ro'])

        # Adding model 'PendingIndex_nl'
        db.create_table(u'dir_pendingindex_nl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_nl'])

        # Adding model 'SiteInfo_cs'
        db.create_table(u'dir_siteinfo_cs', (
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
        db.send_create_signal(u'dir', ['SiteInfo_cs'])

        # Adding model 'SiteInfo_el'
        db.create_table(u'dir_siteinfo_el', (
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
        db.send_create_signal(u'dir', ['SiteInfo_el'])

        # Adding model 'SiteInfo_nl'
        db.create_table(u'dir_siteinfo_nl', (
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
        db.send_create_signal(u'dir', ['SiteInfo_nl'])

        # Adding model 'PendingIndex_da'
        db.create_table(u'dir_pendingindex_da', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_da'])

        # Adding model 'IndexTerm_da'
        db.create_table(u'dir_indexterm_da', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_da'])

        # Adding model 'PendingIndex_hu'
        db.create_table(u'dir_pendingindex_hu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_hu'])

        # Adding model 'SiteInfo_sw'
        db.create_table(u'dir_siteinfo_sw', (
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
        db.send_create_signal(u'dir', ['SiteInfo_sw'])

        # Adding model 'IndexTerm_nl'
        db.create_table(u'dir_indexterm_nl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_nl'])

        # Adding model 'PendingIndex_sw'
        db.create_table(u'dir_pendingindex_sw', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_sw'])

        # Adding model 'SiteInfo_da'
        db.create_table(u'dir_siteinfo_da', (
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
        db.send_create_signal(u'dir', ['SiteInfo_da'])

        # Adding model 'PendingIndex_cs'
        db.create_table(u'dir_pendingindex_cs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_cs'])

        # Adding model 'SiteInfo_ro'
        db.create_table(u'dir_siteinfo_ro', (
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
        db.send_create_signal(u'dir', ['SiteInfo_ro'])

        # Adding model 'SiteInfo_hu'
        db.create_table(u'dir_siteinfo_hu', (
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
        db.send_create_signal(u'dir', ['SiteInfo_hu'])

        # Adding model 'PendingIndex_el'
        db.create_table(u'dir_pendingindex_el', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_el'])

        # Adding model 'IndexTerm_cs'
        db.create_table(u'dir_indexterm_cs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_cs'])

        # Adding model 'IndexTerm_el'
        db.create_table(u'dir_indexterm_el', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_el'])

        # Adding model 'IndexTerm_hu'
        db.create_table(u'dir_indexterm_hu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_hu'])

        # Adding model 'IndexTerm_ro'
        db.create_table(u'dir_indexterm_ro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_ro'])


    def backwards(self, orm):
        # Deleting model 'IndexTerm_sw'
        db.delete_table(u'dir_indexterm_sw')

        # Deleting model 'PendingIndex_ro'
        db.delete_table(u'dir_pendingindex_ro')

        # Deleting model 'PendingIndex_nl'
        db.delete_table(u'dir_pendingindex_nl')

        # Deleting model 'SiteInfo_cs'
        db.delete_table(u'dir_siteinfo_cs')

        # Deleting model 'SiteInfo_el'
        db.delete_table(u'dir_siteinfo_el')

        # Deleting model 'SiteInfo_nl'
        db.delete_table(u'dir_siteinfo_nl')

        # Deleting model 'PendingIndex_da'
        db.delete_table(u'dir_pendingindex_da')

        # Deleting model 'IndexTerm_da'
        db.delete_table(u'dir_indexterm_da')

        # Deleting model 'PendingIndex_hu'
        db.delete_table(u'dir_pendingindex_hu')

        # Deleting model 'SiteInfo_sw'
        db.delete_table(u'dir_siteinfo_sw')

        # Deleting model 'IndexTerm_nl'
        db.delete_table(u'dir_indexterm_nl')

        # Deleting model 'PendingIndex_sw'
        db.delete_table(u'dir_pendingindex_sw')

        # Deleting model 'SiteInfo_da'
        db.delete_table(u'dir_siteinfo_da')

        # Deleting model 'PendingIndex_cs'
        db.delete_table(u'dir_pendingindex_cs')

        # Deleting model 'SiteInfo_ro'
        db.delete_table(u'dir_siteinfo_ro')

        # Deleting model 'SiteInfo_hu'
        db.delete_table(u'dir_siteinfo_hu')

        # Deleting model 'PendingIndex_el'
        db.delete_table(u'dir_pendingindex_el')

        # Deleting model 'IndexTerm_cs'
        db.delete_table(u'dir_indexterm_cs')

        # Deleting model 'IndexTerm_el'
        db.delete_table(u'dir_indexterm_el')

        # Deleting model 'IndexTerm_hu'
        db.delete_table(u'dir_indexterm_hu')

        # Deleting model 'IndexTerm_ro'
        db.delete_table(u'dir_indexterm_ro')


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
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_cs': {
            'Meta': {'object_name': 'IndexTerm_cs'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_da': {
            'Meta': {'object_name': 'IndexTerm_da'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_el': {
            'Meta': {'object_name': 'IndexTerm_el'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fi': {
            'Meta': {'object_name': 'IndexTerm_fi'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_hu': {
            'Meta': {'object_name': 'IndexTerm_hu'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_is': {
            'Meta': {'object_name': 'IndexTerm_is'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_it': {
            'Meta': {'object_name': 'IndexTerm_it'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_nl': {
            'Meta': {'object_name': 'IndexTerm_nl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_no': {
            'Meta': {'object_name': 'IndexTerm_no'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pl': {
            'Meta': {'object_name': 'IndexTerm_pl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pt': {
            'Meta': {'object_name': 'IndexTerm_pt'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_ro': {
            'Meta': {'object_name': 'IndexTerm_ro'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sv': {
            'Meta': {'object_name': 'IndexTerm_sv'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sw': {
            'Meta': {'object_name': 'IndexTerm_sw'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
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
        }
    }

    complete_apps = ['dir']