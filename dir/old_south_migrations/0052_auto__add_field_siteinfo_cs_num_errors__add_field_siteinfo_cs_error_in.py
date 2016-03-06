# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SiteInfo_cs.num_errors'
        db.add_column(u'dir_siteinfo_cs', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_cs.error_info'
        db.add_column(u'dir_siteinfo_cs', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sw.num_errors'
        db.add_column(u'dir_siteinfo_sw', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sw.error_info'
        db.add_column(u'dir_siteinfo_sw', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sv.num_errors'
        db.add_column(u'dir_siteinfo_sv', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sv.error_info'
        db.add_column(u'dir_siteinfo_sv', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sk.num_errors'
        db.add_column(u'dir_siteinfo_sk', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sk.error_info'
        db.add_column(u'dir_siteinfo_sk', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sl.num_errors'
        db.add_column(u'dir_siteinfo_sl', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_sl.error_info'
        db.add_column(u'dir_siteinfo_sl', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_hu.num_errors'
        db.add_column(u'dir_siteinfo_hu', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_hu.error_info'
        db.add_column(u'dir_siteinfo_hu', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_hr.num_errors'
        db.add_column(u'dir_siteinfo_hr', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_hr.error_info'
        db.add_column(u'dir_siteinfo_hr', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.num_errors'
        db.add_column(u'dir_siteinfo_es', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_es.error_info'
        db.add_column(u'dir_siteinfo_es', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_et.num_errors'
        db.add_column(u'dir_siteinfo_et', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_et.error_info'
        db.add_column(u'dir_siteinfo_et', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_el.num_errors'
        db.add_column(u'dir_siteinfo_el', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_el.error_info'
        db.add_column(u'dir_siteinfo_el', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_ro.num_errors'
        db.add_column(u'dir_siteinfo_ro', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_ro.error_info'
        db.add_column(u'dir_siteinfo_ro', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_da.num_errors'
        db.add_column(u'dir_siteinfo_da', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_da.error_info'
        db.add_column(u'dir_siteinfo_da', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.num_errors'
        db.add_column(u'dir_siteinfo_de', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_de.error_info'
        db.add_column(u'dir_siteinfo_de', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_lt.num_errors'
        db.add_column(u'dir_siteinfo_lt', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_lt.error_info'
        db.add_column(u'dir_siteinfo_lt', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_lv.num_errors'
        db.add_column(u'dir_siteinfo_lv', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_lv.error_info'
        db.add_column(u'dir_siteinfo_lv', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_tr.num_errors'
        db.add_column(u'dir_siteinfo_tr', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_tr.error_info'
        db.add_column(u'dir_siteinfo_tr', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_pt.num_errors'
        db.add_column(u'dir_siteinfo_pt', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_pt.error_info'
        db.add_column(u'dir_siteinfo_pt', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_pl.num_errors'
        db.add_column(u'dir_siteinfo_pl', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_pl.error_info'
        db.add_column(u'dir_siteinfo_pl', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_it.num_errors'
        db.add_column(u'dir_siteinfo_it', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_it.error_info'
        db.add_column(u'dir_siteinfo_it', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_is.num_errors'
        db.add_column(u'dir_siteinfo_is', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_is.error_info'
        db.add_column(u'dir_siteinfo_is', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.num_errors'
        db.add_column(u'dir_siteinfo_fr', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fr.error_info'
        db.add_column(u'dir_siteinfo_fr', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_no.num_errors'
        db.add_column(u'dir_siteinfo_no', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_no.error_info'
        db.add_column(u'dir_siteinfo_no', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_nl.num_errors'
        db.add_column(u'dir_siteinfo_nl', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_nl.error_info'
        db.add_column(u'dir_siteinfo_nl', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fi.num_errors'
        db.add_column(u'dir_siteinfo_fi', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo_fi.error_info'
        db.add_column(u'dir_siteinfo_fi', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo.num_errors'
        db.add_column('site_info', 'num_errors',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'SiteInfo.error_info'
        db.add_column('site_info', 'error_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SiteInfo_cs.num_errors'
        db.delete_column(u'dir_siteinfo_cs', 'num_errors')

        # Deleting field 'SiteInfo_cs.error_info'
        db.delete_column(u'dir_siteinfo_cs', 'error_info')

        # Deleting field 'SiteInfo_sw.num_errors'
        db.delete_column(u'dir_siteinfo_sw', 'num_errors')

        # Deleting field 'SiteInfo_sw.error_info'
        db.delete_column(u'dir_siteinfo_sw', 'error_info')

        # Deleting field 'SiteInfo_sv.num_errors'
        db.delete_column(u'dir_siteinfo_sv', 'num_errors')

        # Deleting field 'SiteInfo_sv.error_info'
        db.delete_column(u'dir_siteinfo_sv', 'error_info')

        # Deleting field 'SiteInfo_sk.num_errors'
        db.delete_column(u'dir_siteinfo_sk', 'num_errors')

        # Deleting field 'SiteInfo_sk.error_info'
        db.delete_column(u'dir_siteinfo_sk', 'error_info')

        # Deleting field 'SiteInfo_sl.num_errors'
        db.delete_column(u'dir_siteinfo_sl', 'num_errors')

        # Deleting field 'SiteInfo_sl.error_info'
        db.delete_column(u'dir_siteinfo_sl', 'error_info')

        # Deleting field 'SiteInfo_hu.num_errors'
        db.delete_column(u'dir_siteinfo_hu', 'num_errors')

        # Deleting field 'SiteInfo_hu.error_info'
        db.delete_column(u'dir_siteinfo_hu', 'error_info')

        # Deleting field 'SiteInfo_hr.num_errors'
        db.delete_column(u'dir_siteinfo_hr', 'num_errors')

        # Deleting field 'SiteInfo_hr.error_info'
        db.delete_column(u'dir_siteinfo_hr', 'error_info')

        # Deleting field 'SiteInfo_es.num_errors'
        db.delete_column(u'dir_siteinfo_es', 'num_errors')

        # Deleting field 'SiteInfo_es.error_info'
        db.delete_column(u'dir_siteinfo_es', 'error_info')

        # Deleting field 'SiteInfo_et.num_errors'
        db.delete_column(u'dir_siteinfo_et', 'num_errors')

        # Deleting field 'SiteInfo_et.error_info'
        db.delete_column(u'dir_siteinfo_et', 'error_info')

        # Deleting field 'SiteInfo_el.num_errors'
        db.delete_column(u'dir_siteinfo_el', 'num_errors')

        # Deleting field 'SiteInfo_el.error_info'
        db.delete_column(u'dir_siteinfo_el', 'error_info')

        # Deleting field 'SiteInfo_ro.num_errors'
        db.delete_column(u'dir_siteinfo_ro', 'num_errors')

        # Deleting field 'SiteInfo_ro.error_info'
        db.delete_column(u'dir_siteinfo_ro', 'error_info')

        # Deleting field 'SiteInfo_da.num_errors'
        db.delete_column(u'dir_siteinfo_da', 'num_errors')

        # Deleting field 'SiteInfo_da.error_info'
        db.delete_column(u'dir_siteinfo_da', 'error_info')

        # Deleting field 'SiteInfo_de.num_errors'
        db.delete_column(u'dir_siteinfo_de', 'num_errors')

        # Deleting field 'SiteInfo_de.error_info'
        db.delete_column(u'dir_siteinfo_de', 'error_info')

        # Deleting field 'SiteInfo_lt.num_errors'
        db.delete_column(u'dir_siteinfo_lt', 'num_errors')

        # Deleting field 'SiteInfo_lt.error_info'
        db.delete_column(u'dir_siteinfo_lt', 'error_info')

        # Deleting field 'SiteInfo_lv.num_errors'
        db.delete_column(u'dir_siteinfo_lv', 'num_errors')

        # Deleting field 'SiteInfo_lv.error_info'
        db.delete_column(u'dir_siteinfo_lv', 'error_info')

        # Deleting field 'SiteInfo_tr.num_errors'
        db.delete_column(u'dir_siteinfo_tr', 'num_errors')

        # Deleting field 'SiteInfo_tr.error_info'
        db.delete_column(u'dir_siteinfo_tr', 'error_info')

        # Deleting field 'SiteInfo_pt.num_errors'
        db.delete_column(u'dir_siteinfo_pt', 'num_errors')

        # Deleting field 'SiteInfo_pt.error_info'
        db.delete_column(u'dir_siteinfo_pt', 'error_info')

        # Deleting field 'SiteInfo_pl.num_errors'
        db.delete_column(u'dir_siteinfo_pl', 'num_errors')

        # Deleting field 'SiteInfo_pl.error_info'
        db.delete_column(u'dir_siteinfo_pl', 'error_info')

        # Deleting field 'SiteInfo_it.num_errors'
        db.delete_column(u'dir_siteinfo_it', 'num_errors')

        # Deleting field 'SiteInfo_it.error_info'
        db.delete_column(u'dir_siteinfo_it', 'error_info')

        # Deleting field 'SiteInfo_is.num_errors'
        db.delete_column(u'dir_siteinfo_is', 'num_errors')

        # Deleting field 'SiteInfo_is.error_info'
        db.delete_column(u'dir_siteinfo_is', 'error_info')

        # Deleting field 'SiteInfo_fr.num_errors'
        db.delete_column(u'dir_siteinfo_fr', 'num_errors')

        # Deleting field 'SiteInfo_fr.error_info'
        db.delete_column(u'dir_siteinfo_fr', 'error_info')

        # Deleting field 'SiteInfo_no.num_errors'
        db.delete_column(u'dir_siteinfo_no', 'num_errors')

        # Deleting field 'SiteInfo_no.error_info'
        db.delete_column(u'dir_siteinfo_no', 'error_info')

        # Deleting field 'SiteInfo_nl.num_errors'
        db.delete_column(u'dir_siteinfo_nl', 'num_errors')

        # Deleting field 'SiteInfo_nl.error_info'
        db.delete_column(u'dir_siteinfo_nl', 'error_info')

        # Deleting field 'SiteInfo_fi.num_errors'
        db.delete_column(u'dir_siteinfo_fi', 'num_errors')

        # Deleting field 'SiteInfo_fi.error_info'
        db.delete_column(u'dir_siteinfo_fi', 'error_info')

        # Deleting field 'SiteInfo.num_errors'
        db.delete_column('site_info', 'num_errors')

        # Deleting field 'SiteInfo.error_info'
        db.delete_column('site_info', 'error_info')


    models = {
        u'dir.changelogitem': {
            'Meta': {'object_name': 'ChangelogItem'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_domains_blocked': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_terms_indexed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_urls_crawled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.domainextension': {
            'Meta': {'object_name': 'DomainExtension'},
            'default_language': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_new_domain_urls': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.domaininfo': {
            'Meta': {'object_name': 'DomainInfo'},
            'alexa_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alexa_rank_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_association': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'max_urls': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rank_adjustment': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rank_reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'uses_language_subdirs': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.excludedsite': {
            'Meta': {'object_name': 'ExcludedSite', 'db_table': "'excluded_site'"},
            'detailedreason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exclude_subdomains': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'dir.feedbackitem': {
            'Meta': {'object_name': 'FeedbackItem'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'num_search_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.indexterm': {
            'Meta': {'object_name': 'IndexTerm'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_cs': {
            'Meta': {'object_name': 'IndexTerm_cs'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_da': {
            'Meta': {'object_name': 'IndexTerm_da'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_el': {
            'Meta': {'object_name': 'IndexTerm_el'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_et': {
            'Meta': {'object_name': 'IndexTerm_et'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fi': {
            'Meta': {'object_name': 'IndexTerm_fi'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_hr': {
            'Meta': {'object_name': 'IndexTerm_hr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_hu': {
            'Meta': {'object_name': 'IndexTerm_hu'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_is': {
            'Meta': {'object_name': 'IndexTerm_is'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_it': {
            'Meta': {'object_name': 'IndexTerm_it'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_lt': {
            'Meta': {'object_name': 'IndexTerm_lt'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_lv': {
            'Meta': {'object_name': 'IndexTerm_lv'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_nl': {
            'Meta': {'object_name': 'IndexTerm_nl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_no': {
            'Meta': {'object_name': 'IndexTerm_no'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_pl': {
            'Meta': {'object_name': 'IndexTerm_pl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_pt': {
            'Meta': {'object_name': 'IndexTerm_pt'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ro': {
            'Meta': {'object_name': 'IndexTerm_ro'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sk': {
            'Meta': {'object_name': 'IndexTerm_sk'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sl': {
            'Meta': {'object_name': 'IndexTerm_sl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sv': {
            'Meta': {'object_name': 'IndexTerm_sv'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sw': {
            'Meta': {'object_name': 'IndexTerm_sw'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_tr': {
            'Meta': {'object_name': 'IndexTerm_tr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dir.ipaddress': {
            'Meta': {'object_name': 'IPAddress'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'spam_commenter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        u'dir.pendingindex_et': {
            'Meta': {'object_name': 'PendingIndex_et'},
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
        u'dir.pendingindex_sl': {
            'Meta': {'object_name': 'PendingIndex_sl'},
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
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_cs': {
            'Meta': {'object_name': 'SearchLog_cs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_da': {
            'Meta': {'object_name': 'SearchLog_da'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_de': {
            'Meta': {'object_name': 'SearchLog_de'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_el': {
            'Meta': {'object_name': 'SearchLog_el'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_es': {
            'Meta': {'object_name': 'SearchLog_es'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_et': {
            'Meta': {'object_name': 'SearchLog_et'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fi': {
            'Meta': {'object_name': 'SearchLog_fi'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fr': {
            'Meta': {'object_name': 'SearchLog_fr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hr': {
            'Meta': {'object_name': 'SearchLog_hr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hu': {
            'Meta': {'object_name': 'SearchLog_hu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_is': {
            'Meta': {'object_name': 'SearchLog_is'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_it': {
            'Meta': {'object_name': 'SearchLog_it'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lt': {
            'Meta': {'object_name': 'SearchLog_lt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lv': {
            'Meta': {'object_name': 'SearchLog_lv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nl': {
            'Meta': {'object_name': 'SearchLog_nl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_no': {
            'Meta': {'object_name': 'SearchLog_no'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pl': {
            'Meta': {'object_name': 'SearchLog_pl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pt': {
            'Meta': {'object_name': 'SearchLog_pt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ro': {
            'Meta': {'object_name': 'SearchLog_ro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sk': {
            'Meta': {'object_name': 'SearchLog_sk'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sl': {
            'Meta': {'object_name': 'SearchLog_sl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sv': {
            'Meta': {'object_name': 'SearchLog_sv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sw': {
            'Meta': {'object_name': 'SearchLog_sw'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_tr': {
            'Meta': {'object_name': 'SearchLog_tr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.setting': {
            'Meta': {'object_name': 'Setting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'dir.siteinfo': {
            'Meta': {'object_name': 'SiteInfo', 'db_table': "'site_info'"},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_cs': {
            'Meta': {'object_name': 'SiteInfo_cs'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_da': {
            'Meta': {'object_name': 'SiteInfo_da'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_de': {
            'Meta': {'object_name': 'SiteInfo_de'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_el': {
            'Meta': {'object_name': 'SiteInfo_el'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_es': {
            'Meta': {'object_name': 'SiteInfo_es'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_et': {
            'Meta': {'object_name': 'SiteInfo_et'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_fi': {
            'Meta': {'object_name': 'SiteInfo_fi'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_fr': {
            'Meta': {'object_name': 'SiteInfo_fr'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_hr': {
            'Meta': {'object_name': 'SiteInfo_hr'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_hu': {
            'Meta': {'object_name': 'SiteInfo_hu'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_is': {
            'Meta': {'object_name': 'SiteInfo_is'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_it': {
            'Meta': {'object_name': 'SiteInfo_it'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_lt': {
            'Meta': {'object_name': 'SiteInfo_lt'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_lv': {
            'Meta': {'object_name': 'SiteInfo_lv'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_nl': {
            'Meta': {'object_name': 'SiteInfo_nl'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_no': {
            'Meta': {'object_name': 'SiteInfo_no'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_pl': {
            'Meta': {'object_name': 'SiteInfo_pl'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_pt': {
            'Meta': {'object_name': 'SiteInfo_pt'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_ro': {
            'Meta': {'object_name': 'SiteInfo_ro'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_sk': {
            'Meta': {'object_name': 'SiteInfo_sk'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_sl': {
            'Meta': {'object_name': 'SiteInfo_sl'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_sv': {
            'Meta': {'object_name': 'SiteInfo_sv'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_sw': {
            'Meta': {'object_name': 'SiteInfo_sw'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        },
        u'dir.siteinfo_tr': {
            'Meta': {'object_name': 'SiteInfo_tr'},
            'error_info': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2048', 'blank': 'True'})
        }
    }

    complete_apps = ['dir']