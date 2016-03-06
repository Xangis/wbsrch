# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SiteInfo_fr.siteinfo_ptr'
        db.delete_column(u'dir_siteinfo_fr', u'siteinfo_ptr_id')

        # Adding field 'SiteInfo_fr.id'
        db.add_column(u'dir_siteinfo_fr', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.rooturl'
        db.add_column(u'dir_siteinfo_fr', 'rooturl',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.url'
        db.add_column(u'dir_siteinfo_fr', 'url',
                      self.gf('django.db.models.fields.TextField')(default='', unique=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.lastcrawled'
        db.add_column(u'dir_siteinfo_fr', 'lastcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.firstcrawled'
        db.add_column(u'dir_siteinfo_fr', 'firstcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagetitle'
        db.add_column(u'dir_siteinfo_fr', 'pagetitle',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagedescription'
        db.add_column(u'dir_siteinfo_fr', 'pagedescription',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagefirstheadtag'
        db.add_column(u'dir_siteinfo_fr', 'pagefirstheadtag',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagesize'
        db.add_column(u'dir_siteinfo_fr', 'pagesize',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagecontents'
        db.add_column(u'dir_siteinfo_fr', 'pagecontents',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagekeywords'
        db.add_column(u'dir_siteinfo_fr', 'pagekeywords',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.pagetext'
        db.add_column(u'dir_siteinfo_fr', 'pagetext',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SiteInfo_es.siteinfo_ptr'
        db.delete_column(u'dir_siteinfo_es', u'siteinfo_ptr_id')

        # Adding field 'SiteInfo_es.id'
        db.add_column(u'dir_siteinfo_es', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.rooturl'
        db.add_column(u'dir_siteinfo_es', 'rooturl',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.url'
        db.add_column(u'dir_siteinfo_es', 'url',
                      self.gf('django.db.models.fields.TextField')(default='', unique=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.lastcrawled'
        db.add_column(u'dir_siteinfo_es', 'lastcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.firstcrawled'
        db.add_column(u'dir_siteinfo_es', 'firstcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagetitle'
        db.add_column(u'dir_siteinfo_es', 'pagetitle',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagedescription'
        db.add_column(u'dir_siteinfo_es', 'pagedescription',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagefirstheadtag'
        db.add_column(u'dir_siteinfo_es', 'pagefirstheadtag',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagesize'
        db.add_column(u'dir_siteinfo_es', 'pagesize',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagecontents'
        db.add_column(u'dir_siteinfo_es', 'pagecontents',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagekeywords'
        db.add_column(u'dir_siteinfo_es', 'pagekeywords',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.pagetext'
        db.add_column(u'dir_siteinfo_es', 'pagetext',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SiteInfo_de.siteinfo_ptr'
        db.delete_column(u'dir_siteinfo_de', u'siteinfo_ptr_id')

        # Adding field 'SiteInfo_de.id'
        db.add_column(u'dir_siteinfo_de', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.rooturl'
        db.add_column(u'dir_siteinfo_de', 'rooturl',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.url'
        db.add_column(u'dir_siteinfo_de', 'url',
                      self.gf('django.db.models.fields.TextField')(default='', unique=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.lastcrawled'
        db.add_column(u'dir_siteinfo_de', 'lastcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.firstcrawled'
        db.add_column(u'dir_siteinfo_de', 'firstcrawled',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagetitle'
        db.add_column(u'dir_siteinfo_de', 'pagetitle',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagedescription'
        db.add_column(u'dir_siteinfo_de', 'pagedescription',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagefirstheadtag'
        db.add_column(u'dir_siteinfo_de', 'pagefirstheadtag',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagesize'
        db.add_column(u'dir_siteinfo_de', 'pagesize',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagecontents'
        db.add_column(u'dir_siteinfo_de', 'pagecontents',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagekeywords'
        db.add_column(u'dir_siteinfo_de', 'pagekeywords',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.pagetext'
        db.add_column(u'dir_siteinfo_de', 'pagetext',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SiteInfo_fr.siteinfo_ptr'
        raise RuntimeError("Cannot reverse this migration. 'SiteInfo_fr.siteinfo_ptr' and its values cannot be restored.")
        # Deleting field 'SiteInfo_fr.id'
        db.delete_column(u'dir_siteinfo_fr', u'id')

        # Deleting field 'SiteInfo_fr.rooturl'
        db.delete_column(u'dir_siteinfo_fr', 'rooturl')

        # Deleting field 'SiteInfo_fr.url'
        db.delete_column(u'dir_siteinfo_fr', 'url')

        # Deleting field 'SiteInfo_fr.lastcrawled'
        db.delete_column(u'dir_siteinfo_fr', 'lastcrawled')

        # Deleting field 'SiteInfo_fr.firstcrawled'
        db.delete_column(u'dir_siteinfo_fr', 'firstcrawled')

        # Deleting field 'SiteInfo_fr.pagetitle'
        db.delete_column(u'dir_siteinfo_fr', 'pagetitle')

        # Deleting field 'SiteInfo_fr.pagedescription'
        db.delete_column(u'dir_siteinfo_fr', 'pagedescription')

        # Deleting field 'SiteInfo_fr.pagefirstheadtag'
        db.delete_column(u'dir_siteinfo_fr', 'pagefirstheadtag')

        # Deleting field 'SiteInfo_fr.pagesize'
        db.delete_column(u'dir_siteinfo_fr', 'pagesize')

        # Deleting field 'SiteInfo_fr.pagecontents'
        db.delete_column(u'dir_siteinfo_fr', 'pagecontents')

        # Deleting field 'SiteInfo_fr.pagekeywords'
        db.delete_column(u'dir_siteinfo_fr', 'pagekeywords')

        # Deleting field 'SiteInfo_fr.pagetext'
        db.delete_column(u'dir_siteinfo_fr', 'pagetext')

        # Adding field 'SiteInfo_es.siteinfo_ptr'
        db.add_column(u'dir_siteinfo_es', u'siteinfo_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['dir.SiteInfo'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'SiteInfo_es.id'
        db.delete_column(u'dir_siteinfo_es', u'id')

        # Deleting field 'SiteInfo_es.rooturl'
        db.delete_column(u'dir_siteinfo_es', 'rooturl')

        # Deleting field 'SiteInfo_es.url'
        db.delete_column(u'dir_siteinfo_es', 'url')

        # Deleting field 'SiteInfo_es.lastcrawled'
        db.delete_column(u'dir_siteinfo_es', 'lastcrawled')

        # Deleting field 'SiteInfo_es.firstcrawled'
        db.delete_column(u'dir_siteinfo_es', 'firstcrawled')

        # Deleting field 'SiteInfo_es.pagetitle'
        db.delete_column(u'dir_siteinfo_es', 'pagetitle')

        # Deleting field 'SiteInfo_es.pagedescription'
        db.delete_column(u'dir_siteinfo_es', 'pagedescription')

        # Deleting field 'SiteInfo_es.pagefirstheadtag'
        db.delete_column(u'dir_siteinfo_es', 'pagefirstheadtag')

        # Deleting field 'SiteInfo_es.pagesize'
        db.delete_column(u'dir_siteinfo_es', 'pagesize')

        # Deleting field 'SiteInfo_es.pagecontents'
        db.delete_column(u'dir_siteinfo_es', 'pagecontents')

        # Deleting field 'SiteInfo_es.pagekeywords'
        db.delete_column(u'dir_siteinfo_es', 'pagekeywords')

        # Deleting field 'SiteInfo_es.pagetext'
        db.delete_column(u'dir_siteinfo_es', 'pagetext')

        # Adding field 'SiteInfo_de.siteinfo_ptr'
        db.add_column(u'dir_siteinfo_de', u'siteinfo_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['dir.SiteInfo'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'SiteInfo_de.id'
        db.delete_column(u'dir_siteinfo_de', u'id')

        # Deleting field 'SiteInfo_de.rooturl'
        db.delete_column(u'dir_siteinfo_de', 'rooturl')

        # Deleting field 'SiteInfo_de.url'
        db.delete_column(u'dir_siteinfo_de', 'url')

        # Deleting field 'SiteInfo_de.lastcrawled'
        db.delete_column(u'dir_siteinfo_de', 'lastcrawled')

        # Deleting field 'SiteInfo_de.firstcrawled'
        db.delete_column(u'dir_siteinfo_de', 'firstcrawled')

        # Deleting field 'SiteInfo_de.pagetitle'
        db.delete_column(u'dir_siteinfo_de', 'pagetitle')

        # Deleting field 'SiteInfo_de.pagedescription'
        db.delete_column(u'dir_siteinfo_de', 'pagedescription')

        # Deleting field 'SiteInfo_de.pagefirstheadtag'
        db.delete_column(u'dir_siteinfo_de', 'pagefirstheadtag')

        # Deleting field 'SiteInfo_de.pagesize'
        db.delete_column(u'dir_siteinfo_de', 'pagesize')

        # Deleting field 'SiteInfo_de.pagecontents'
        db.delete_column(u'dir_siteinfo_de', 'pagecontents')

        # Deleting field 'SiteInfo_de.pagekeywords'
        db.delete_column(u'dir_siteinfo_de', 'pagekeywords')

        # Deleting field 'SiteInfo_de.pagetext'
        db.delete_column(u'dir_siteinfo_de', 'pagetext')


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
        }
    }

    complete_apps = ['dir']
