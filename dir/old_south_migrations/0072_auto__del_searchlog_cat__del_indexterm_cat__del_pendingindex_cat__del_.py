# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming model 'PendingIndex_si'
        db.rename_table(u'dir_pendingindex_cat', u'dir_pendingindex_ca')

        # Renaming model 'SiteInfo_si'
        db.rename_table(u'dir_siteinfo_cat', u'dir_siteinfo_ca')

        # Renaming model 'SearchLog_si'
        db.rename_table(u'dir_searchlog_cat', u'dir_searchlog_ca')

        # Renaming model 'IndexTerm_si'
        db.rename_table(u'dir_indexterm_cat', u'dir_indexterm_ca')

        # Adding model 'IndexTerm_oc'
        db.create_table(u'dir_indexterm_oc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_oc'])

        # Adding model 'SiteInfo_pms'
        db.create_table(u'dir_siteinfo_pms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_pms'])

        # Adding model 'IndexTerm_fy'
        db.create_table(u'dir_indexterm_fy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_fy'])

        # Adding model 'SiteInfo_scn'
        db.create_table(u'dir_siteinfo_scn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_scn'])

        # Adding model 'SiteInfo_nap'
        db.create_table(u'dir_siteinfo_nap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_nap'])

        # Adding model 'IndexTerm_fo'
        db.create_table(u'dir_indexterm_fo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_fo'])

        # Adding model 'PendingIndex_sc'
        db.create_table(u'dir_pendingindex_sc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_sc'])

        # Adding model 'IndexTerm_vec'
        db.create_table(u'dir_indexterm_vec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_vec'])

        # Adding model 'SiteInfo_sc'
        db.create_table(u'dir_siteinfo_sc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_sc'])

        # Adding model 'SiteInfo_oc'
        db.create_table(u'dir_siteinfo_oc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_oc'])

        # Adding model 'SearchLog_sc'
        db.create_table(u'dir_searchlog_sc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_sc'])

        # Adding model 'IndexTerm_eu'
        db.create_table(u'dir_indexterm_eu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_eu'])

        # Adding model 'SearchLog_nap'
        db.create_table(u'dir_searchlog_nap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_nap'])

        # Adding model 'SearchLog_scn'
        db.create_table(u'dir_searchlog_scn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_scn'])

        # Adding model 'SearchLog_fy'
        db.create_table(u'dir_searchlog_fy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_fy'])

        # Adding model 'IndexTerm_nap'
        db.create_table(u'dir_indexterm_nap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_nap'])

        # Adding model 'SiteInfo_fy'
        db.create_table(u'dir_siteinfo_fy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_fy'])

        # Adding model 'IndexTerm_scn'
        db.create_table(u'dir_indexterm_scn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_scn'])

        # Adding model 'SearchLog_eu'
        db.create_table(u'dir_searchlog_eu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_eu'])

        # Adding model 'PendingIndex_pms'
        db.create_table(u'dir_pendingindex_pms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_pms'])

        # Adding model 'IndexTerm_sc'
        db.create_table(u'dir_indexterm_sc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_sc'])

        # Adding model 'SearchLog_oc'
        db.create_table(u'dir_searchlog_oc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_oc'])

        # Adding model 'SearchLog_vec'
        db.create_table(u'dir_searchlog_vec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_vec'])

        # Adding model 'PendingIndex_fy'
        db.create_table(u'dir_pendingindex_fy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_fy'])

        # Adding model 'PendingIndex_fo'
        db.create_table(u'dir_pendingindex_fo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_fo'])

        # Adding model 'SearchLog_fo'
        db.create_table(u'dir_searchlog_fo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_fo'])

        # Adding model 'SearchLog_gl'
        db.create_table(u'dir_searchlog_gl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_gl'])

        # Adding model 'PendingIndex_oc'
        db.create_table(u'dir_pendingindex_oc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_oc'])

        # Adding model 'PendingIndex_gl'
        db.create_table(u'dir_pendingindex_gl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_gl'])

        # Adding model 'SearchLog_pms'
        db.create_table(u'dir_searchlog_pms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('result_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_search', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('search_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('indexed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('browserstring', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['SearchLog_pms'])

        # Adding model 'PendingIndex_scn'
        db.create_table(u'dir_pendingindex_scn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_scn'])

        # Adding model 'SiteInfo_vec'
        db.create_table(u'dir_siteinfo_vec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_vec'])

        # Adding model 'PendingIndex_vec'
        db.create_table(u'dir_pendingindex_vec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_vec'])

        # Adding model 'IndexTerm_gl'
        db.create_table(u'dir_indexterm_gl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_gl'])

        # Adding model 'IndexTerm_pms'
        db.create_table(u'dir_indexterm_pms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_rankings', self.gf('django.db.models.fields.TextField')()),
            ('num_results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('search_results', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actively_blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('refused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('typo_for', self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True)),
            ('is_language', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['IndexTerm_pms'])

        # Adding model 'SiteInfo_fo'
        db.create_table(u'dir_siteinfo_fo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooturl', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2048, blank=True)),
            ('pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagedescription', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('pagecontents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagetext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pagesize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lastcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('firstcrawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('error_info', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'dir', ['SiteInfo_fo'])

        # Adding model 'PendingIndex_nap'
        db.create_table(u'dir_pendingindex_nap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_nap'])

        # Adding model 'PendingIndex_eu'
        db.create_table(u'dir_pendingindex_eu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(unique=True, max_length=240)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dir', ['PendingIndex_eu'])

        # Adding field 'IndexTerm_om.is_language'
        db.add_column(u'dir_indexterm_om', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_lt.is_language'
        db.add_column(u'dir_indexterm_lt', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_wo.is_language'
        db.add_column(u'dir_indexterm_wo', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_kg.is_language'
        db.add_column(u'dir_indexterm_kg', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_fr.is_language'
        db.add_column(u'dir_indexterm_fr', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ff.is_language'
        db.add_column(u'dir_indexterm_ff', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_no.is_language'
        db.add_column(u'dir_indexterm_no', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_nl.is_language'
        db.add_column(u'dir_indexterm_nl', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ny.is_language'
        db.add_column(u'dir_indexterm_ny', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_es.is_language'
        db.add_column(u'dir_indexterm_es', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_et.is_language'
        db.add_column(u'dir_indexterm_et', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_nso.is_language'
        db.add_column(u'dir_indexterm_nso', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_el.is_language'
        db.add_column(u'dir_indexterm_el', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ee.is_language'
        db.add_column(u'dir_indexterm_ee', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ve.is_language'
        db.add_column(u'dir_indexterm_ve', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_it.is_language'
        db.add_column(u'dir_indexterm_it', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_is.is_language'
        db.add_column(u'dir_indexterm_is', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_yo.is_language'
        db.add_column(u'dir_indexterm_yo', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_pt.is_language'
        db.add_column(u'dir_indexterm_pt', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_zu.is_language'
        db.add_column(u'dir_indexterm_zu', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ha.is_language'
        db.add_column(u'dir_indexterm_ha', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_pl.is_language'
        db.add_column(u'dir_indexterm_pl', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_hu.is_language'
        db.add_column(u'dir_indexterm_hu', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_hr.is_language'
        db.add_column(u'dir_indexterm_hr', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_xh.is_language'
        db.add_column(u'dir_indexterm_xh', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_st.is_language'
        db.add_column(u'dir_indexterm_st', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_sw.is_language'
        db.add_column(u'dir_indexterm_sw', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_sv.is_language'
        db.add_column(u'dir_indexterm_sv', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ss.is_language'
        db.add_column(u'dir_indexterm_ss', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_sl.is_language'
        db.add_column(u'dir_indexterm_sl', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_so.is_language'
        db.add_column(u'dir_indexterm_so', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_sn.is_language'
        db.add_column(u'dir_indexterm_sn', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_sk.is_language'
        db.add_column(u'dir_indexterm_sk', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_bm.is_language'
        db.add_column(u'dir_indexterm_bm', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ig.is_language'
        db.add_column(u'dir_indexterm_ig', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_fi.is_language'
        db.add_column(u'dir_indexterm_fi', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_rw.is_language'
        db.add_column(u'dir_indexterm_rw', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_rn.is_language'
        db.add_column(u'dir_indexterm_rn', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ro.is_language'
        db.add_column(u'dir_indexterm_ro', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ak.is_language'
        db.add_column(u'dir_indexterm_ak', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm.is_language'
        db.add_column(u'dir_indexterm', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_da.is_language'
        db.add_column(u'dir_indexterm_da', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_de.is_language'
        db.add_column(u'dir_indexterm_de', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_lg.is_language'
        db.add_column(u'dir_indexterm_lg', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ln.is_language'
        db.add_column(u'dir_indexterm_ln', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_lv.is_language'
        db.add_column(u'dir_indexterm_lv', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_tn.is_language'
        db.add_column(u'dir_indexterm_tn', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_tr.is_language'
        db.add_column(u'dir_indexterm_tr', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ts.is_language'
        db.add_column(u'dir_indexterm_ts', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_ki.is_language'
        db.add_column(u'dir_indexterm_ki', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexTerm_cs.is_language'
        db.add_column(u'dir_indexterm_cs', 'is_language',
                      self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Renaming model 'PendingIndex_si'
        db.rename_table(u'dir_pendingindex_ca', u'dir_pendingindex_cat')

        # Renaming model 'SiteInfo_si'
        db.rename_table(u'dir_siteinfo_ca', u'dir_siteinfo_cat')

        # Renaming model 'SearchLog_si'
        db.rename_table(u'dir_searchlog_ca', u'dir_searchlog_cat')

        # Renaming model 'IndexTerm_si'
        db.rename_table(u'dir_indexterm_ca', u'dir_indexterm_cat')

        # Deleting model 'IndexTerm_oc'
        db.delete_table(u'dir_indexterm_oc')

        # Deleting model 'SiteInfo_pms'
        db.delete_table(u'dir_siteinfo_pms')

        # Deleting model 'IndexTerm_fy'
        db.delete_table(u'dir_indexterm_fy')

        # Deleting model 'SiteInfo_scn'
        db.delete_table(u'dir_siteinfo_scn')

        # Deleting model 'SiteInfo_nap'
        db.delete_table(u'dir_siteinfo_nap')

        # Deleting model 'IndexTerm_fo'
        db.delete_table(u'dir_indexterm_fo')

        # Deleting model 'PendingIndex_sc'
        db.delete_table(u'dir_pendingindex_sc')

        # Deleting model 'IndexTerm_vec'
        db.delete_table(u'dir_indexterm_vec')

        # Deleting model 'SiteInfo_sc'
        db.delete_table(u'dir_siteinfo_sc')

        # Deleting model 'SiteInfo_oc'
        db.delete_table(u'dir_siteinfo_oc')

        # Deleting model 'SearchLog_sc'
        db.delete_table(u'dir_searchlog_sc')

        # Deleting model 'IndexTerm_eu'
        db.delete_table(u'dir_indexterm_eu')

        # Deleting model 'SearchLog_nap'
        db.delete_table(u'dir_searchlog_nap')

        # Deleting model 'SearchLog_scn'
        db.delete_table(u'dir_searchlog_scn')

        # Deleting model 'SearchLog_fy'
        db.delete_table(u'dir_searchlog_fy')

        # Deleting model 'IndexTerm_nap'
        db.delete_table(u'dir_indexterm_nap')

        # Deleting model 'SiteInfo_fy'
        db.delete_table(u'dir_siteinfo_fy')

        # Deleting model 'IndexTerm_scn'
        db.delete_table(u'dir_indexterm_scn')

        # Deleting model 'SearchLog_eu'
        db.delete_table(u'dir_searchlog_eu')

        # Deleting model 'PendingIndex_pms'
        db.delete_table(u'dir_pendingindex_pms')

        # Deleting model 'IndexTerm_sc'
        db.delete_table(u'dir_indexterm_sc')

        # Deleting model 'SearchLog_oc'
        db.delete_table(u'dir_searchlog_oc')

        # Deleting model 'SearchLog_vec'
        db.delete_table(u'dir_searchlog_vec')

        # Deleting model 'PendingIndex_fy'
        db.delete_table(u'dir_pendingindex_fy')

        # Deleting model 'PendingIndex_fo'
        db.delete_table(u'dir_pendingindex_fo')

        # Deleting model 'SearchLog_fo'
        db.delete_table(u'dir_searchlog_fo')

        # Deleting model 'SearchLog_gl'
        db.delete_table(u'dir_searchlog_gl')

        # Deleting model 'PendingIndex_oc'
        db.delete_table(u'dir_pendingindex_oc')

        # Deleting model 'PendingIndex_gl'
        db.delete_table(u'dir_pendingindex_gl')

        # Deleting model 'SearchLog_pms'
        db.delete_table(u'dir_searchlog_pms')

        # Deleting model 'PendingIndex_scn'
        db.delete_table(u'dir_pendingindex_scn')

        # Deleting model 'SiteInfo_vec'
        db.delete_table(u'dir_siteinfo_vec')

        # Deleting model 'PendingIndex_vec'
        db.delete_table(u'dir_pendingindex_vec')

        # Deleting model 'IndexTerm_gl'
        db.delete_table(u'dir_indexterm_gl')

        # Deleting model 'IndexTerm_pms'
        db.delete_table(u'dir_indexterm_pms')

        # Deleting model 'SiteInfo_fo'
        db.delete_table(u'dir_siteinfo_fo')

        # Deleting model 'PendingIndex_nap'
        db.delete_table(u'dir_pendingindex_nap')

        # Deleting model 'PendingIndex_eu'
        db.delete_table(u'dir_pendingindex_eu')

        # Deleting field 'IndexTerm_om.is_language'
        db.delete_column(u'dir_indexterm_om', 'is_language')

        # Deleting field 'IndexTerm_lt.is_language'
        db.delete_column(u'dir_indexterm_lt', 'is_language')

        # Deleting field 'IndexTerm_wo.is_language'
        db.delete_column(u'dir_indexterm_wo', 'is_language')

        # Deleting field 'IndexTerm_kg.is_language'
        db.delete_column(u'dir_indexterm_kg', 'is_language')

        # Deleting field 'IndexTerm_fr.is_language'
        db.delete_column(u'dir_indexterm_fr', 'is_language')

        # Deleting field 'IndexTerm_ff.is_language'
        db.delete_column(u'dir_indexterm_ff', 'is_language')

        # Deleting field 'IndexTerm_no.is_language'
        db.delete_column(u'dir_indexterm_no', 'is_language')

        # Deleting field 'IndexTerm_nl.is_language'
        db.delete_column(u'dir_indexterm_nl', 'is_language')

        # Deleting field 'IndexTerm_ny.is_language'
        db.delete_column(u'dir_indexterm_ny', 'is_language')

        # Deleting field 'IndexTerm_es.is_language'
        db.delete_column(u'dir_indexterm_es', 'is_language')

        # Deleting field 'IndexTerm_et.is_language'
        db.delete_column(u'dir_indexterm_et', 'is_language')

        # Deleting field 'IndexTerm_nso.is_language'
        db.delete_column(u'dir_indexterm_nso', 'is_language')

        # Deleting field 'IndexTerm_el.is_language'
        db.delete_column(u'dir_indexterm_el', 'is_language')

        # Deleting field 'IndexTerm_ee.is_language'
        db.delete_column(u'dir_indexterm_ee', 'is_language')

        # Deleting field 'IndexTerm_ve.is_language'
        db.delete_column(u'dir_indexterm_ve', 'is_language')

        # Deleting field 'IndexTerm_it.is_language'
        db.delete_column(u'dir_indexterm_it', 'is_language')

        # Deleting field 'IndexTerm_is.is_language'
        db.delete_column(u'dir_indexterm_is', 'is_language')

        # Deleting field 'IndexTerm_yo.is_language'
        db.delete_column(u'dir_indexterm_yo', 'is_language')

        # Deleting field 'IndexTerm_pt.is_language'
        db.delete_column(u'dir_indexterm_pt', 'is_language')

        # Deleting field 'IndexTerm_zu.is_language'
        db.delete_column(u'dir_indexterm_zu', 'is_language')

        # Deleting field 'IndexTerm_ha.is_language'
        db.delete_column(u'dir_indexterm_ha', 'is_language')

        # Deleting field 'IndexTerm_pl.is_language'
        db.delete_column(u'dir_indexterm_pl', 'is_language')

        # Deleting field 'IndexTerm_hu.is_language'
        db.delete_column(u'dir_indexterm_hu', 'is_language')

        # Deleting field 'IndexTerm_hr.is_language'
        db.delete_column(u'dir_indexterm_hr', 'is_language')

        # Deleting field 'IndexTerm_xh.is_language'
        db.delete_column(u'dir_indexterm_xh', 'is_language')

        # Deleting field 'IndexTerm_st.is_language'
        db.delete_column(u'dir_indexterm_st', 'is_language')

        # Deleting field 'IndexTerm_sw.is_language'
        db.delete_column(u'dir_indexterm_sw', 'is_language')

        # Deleting field 'IndexTerm_sv.is_language'
        db.delete_column(u'dir_indexterm_sv', 'is_language')

        # Deleting field 'IndexTerm_ss.is_language'
        db.delete_column(u'dir_indexterm_ss', 'is_language')

        # Deleting field 'IndexTerm_sl.is_language'
        db.delete_column(u'dir_indexterm_sl', 'is_language')

        # Deleting field 'IndexTerm_so.is_language'
        db.delete_column(u'dir_indexterm_so', 'is_language')

        # Deleting field 'IndexTerm_sn.is_language'
        db.delete_column(u'dir_indexterm_sn', 'is_language')

        # Deleting field 'IndexTerm_sk.is_language'
        db.delete_column(u'dir_indexterm_sk', 'is_language')

        # Deleting field 'IndexTerm_bm.is_language'
        db.delete_column(u'dir_indexterm_bm', 'is_language')

        # Deleting field 'IndexTerm_ig.is_language'
        db.delete_column(u'dir_indexterm_ig', 'is_language')

        # Deleting field 'IndexTerm_fi.is_language'
        db.delete_column(u'dir_indexterm_fi', 'is_language')

        # Deleting field 'IndexTerm_rw.is_language'
        db.delete_column(u'dir_indexterm_rw', 'is_language')

        # Deleting field 'IndexTerm_rn.is_language'
        db.delete_column(u'dir_indexterm_rn', 'is_language')

        # Deleting field 'IndexTerm_ro.is_language'
        db.delete_column(u'dir_indexterm_ro', 'is_language')

        # Deleting field 'IndexTerm_ak.is_language'
        db.delete_column(u'dir_indexterm_ak', 'is_language')

        # Deleting field 'IndexTerm.is_language'
        db.delete_column(u'dir_indexterm', 'is_language')

        # Deleting field 'IndexTerm_da.is_language'
        db.delete_column(u'dir_indexterm_da', 'is_language')

        # Deleting field 'IndexTerm_de.is_language'
        db.delete_column(u'dir_indexterm_de', 'is_language')

        # Deleting field 'IndexTerm_lg.is_language'
        db.delete_column(u'dir_indexterm_lg', 'is_language')

        # Deleting field 'IndexTerm_ln.is_language'
        db.delete_column(u'dir_indexterm_ln', 'is_language')

        # Deleting field 'IndexTerm_lv.is_language'
        db.delete_column(u'dir_indexterm_lv', 'is_language')

        # Deleting field 'IndexTerm_tn.is_language'
        db.delete_column(u'dir_indexterm_tn', 'is_language')

        # Deleting field 'IndexTerm_tr.is_language'
        db.delete_column(u'dir_indexterm_tr', 'is_language')

        # Deleting field 'IndexTerm_ts.is_language'
        db.delete_column(u'dir_indexterm_ts', 'is_language')

        # Deleting field 'IndexTerm_ki.is_language'
        db.delete_column(u'dir_indexterm_ki', 'is_language')

        # Deleting field 'IndexTerm_cs.is_language'
        db.delete_column(u'dir_indexterm_cs', 'is_language')


    models = {
        u'dir.badquery': {
            'Meta': {'ordering': "['keywords']", 'object_name': 'BadQuery'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '260'})
        },
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
            'is_unblockable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_association': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'max_urls': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rank_adjustment': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rank_reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_index': 'True'}),
            'uses_language_query_parameter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uses_language_subdirs': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.excludedsite': {
            'Meta': {'object_name': 'ExcludedSite', 'db_table': "'excluded_site'"},
            'detailedreason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exclude_subdomains': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_index': 'True'})
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
        u'dir.indexstats': {
            'Meta': {'ordering': "['-create_date']", 'object_name': 'IndexStats'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'langs': ('django.db.models.fields.TextField', [], {}),
            'num_excluded': ('django.db.models.fields.IntegerField', [], {}),
            'total_indexes': ('django.db.models.fields.IntegerField', [], {}),
            'total_pendingindexes': ('django.db.models.fields.IntegerField', [], {}),
            'total_urls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'dir.indexterm': {
            'Meta': {'object_name': 'IndexTerm'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'show_ad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ak': {
            'Meta': {'object_name': 'IndexTerm_ak'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_bm': {
            'Meta': {'object_name': 'IndexTerm_bm'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ca': {
            'Meta': {'object_name': 'IndexTerm_ca'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_cs': {
            'Meta': {'object_name': 'IndexTerm_cs'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_da': {
            'Meta': {'object_name': 'IndexTerm_da'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ee': {
            'Meta': {'object_name': 'IndexTerm_ee'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_el': {
            'Meta': {'object_name': 'IndexTerm_el'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_et': {
            'Meta': {'object_name': 'IndexTerm_et'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_eu': {
            'Meta': {'object_name': 'IndexTerm_eu'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ff': {
            'Meta': {'object_name': 'IndexTerm_ff'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fi': {
            'Meta': {'object_name': 'IndexTerm_fi'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fo': {
            'Meta': {'object_name': 'IndexTerm_fo'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_fy': {
            'Meta': {'object_name': 'IndexTerm_fy'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_gl': {
            'Meta': {'object_name': 'IndexTerm_gl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ha': {
            'Meta': {'object_name': 'IndexTerm_ha'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_hr': {
            'Meta': {'object_name': 'IndexTerm_hr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_hu': {
            'Meta': {'object_name': 'IndexTerm_hu'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ig': {
            'Meta': {'object_name': 'IndexTerm_ig'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_is': {
            'Meta': {'object_name': 'IndexTerm_is'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_it': {
            'Meta': {'object_name': 'IndexTerm_it'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_kg': {
            'Meta': {'object_name': 'IndexTerm_kg'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ki': {
            'Meta': {'object_name': 'IndexTerm_ki'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_lg': {
            'Meta': {'object_name': 'IndexTerm_lg'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ln': {
            'Meta': {'object_name': 'IndexTerm_ln'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_lt': {
            'Meta': {'object_name': 'IndexTerm_lt'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_lv': {
            'Meta': {'object_name': 'IndexTerm_lv'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_nap': {
            'Meta': {'object_name': 'IndexTerm_nap'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_nl': {
            'Meta': {'object_name': 'IndexTerm_nl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_no': {
            'Meta': {'object_name': 'IndexTerm_no'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_nso': {
            'Meta': {'object_name': 'IndexTerm_nso'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ny': {
            'Meta': {'object_name': 'IndexTerm_ny'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_oc': {
            'Meta': {'object_name': 'IndexTerm_oc'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_om': {
            'Meta': {'object_name': 'IndexTerm_om'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_pl': {
            'Meta': {'object_name': 'IndexTerm_pl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_pms': {
            'Meta': {'object_name': 'IndexTerm_pms'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_pt': {
            'Meta': {'object_name': 'IndexTerm_pt'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_rn': {
            'Meta': {'object_name': 'IndexTerm_rn'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ro': {
            'Meta': {'object_name': 'IndexTerm_ro'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_rw': {
            'Meta': {'object_name': 'IndexTerm_rw'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sc': {
            'Meta': {'object_name': 'IndexTerm_sc'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_scn': {
            'Meta': {'object_name': 'IndexTerm_scn'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sk': {
            'Meta': {'object_name': 'IndexTerm_sk'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sl': {
            'Meta': {'object_name': 'IndexTerm_sl'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sn': {
            'Meta': {'object_name': 'IndexTerm_sn'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_so': {
            'Meta': {'object_name': 'IndexTerm_so'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ss': {
            'Meta': {'object_name': 'IndexTerm_ss'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_st': {
            'Meta': {'object_name': 'IndexTerm_st'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sv': {
            'Meta': {'object_name': 'IndexTerm_sv'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_sw': {
            'Meta': {'object_name': 'IndexTerm_sw'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_tn': {
            'Meta': {'object_name': 'IndexTerm_tn'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_tr': {
            'Meta': {'object_name': 'IndexTerm_tr'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ts': {
            'Meta': {'object_name': 'IndexTerm_ts'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_ve': {
            'Meta': {'object_name': 'IndexTerm_ve'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_vec': {
            'Meta': {'object_name': 'IndexTerm_vec'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_wo': {
            'Meta': {'object_name': 'IndexTerm_wo'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_xh': {
            'Meta': {'object_name': 'IndexTerm_xh'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_yo': {
            'Meta': {'object_name': 'IndexTerm_yo'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.indexterm_zu': {
            'Meta': {'object_name': 'IndexTerm_zu'},
            'actively_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'is_language': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {}),
            'refused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_results': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'typo_for': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'})
        },
        u'dir.ipaddress': {
            'Meta': {'object_name': 'IPAddress'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'spam_commenter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dir.monthlysearchreport': {
            'Meta': {'ordering': "['-year', '-month', 'language']", 'object_name': 'MonthlySearchReport'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'top_searches': ('django.db.models.fields.TextField', [], {}),
            'total_searches': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'dir.pendingindex': {
            'Meta': {'object_name': 'PendingIndex'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ak': {
            'Meta': {'object_name': 'PendingIndex_ak'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_bm': {
            'Meta': {'object_name': 'PendingIndex_bm'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ca': {
            'Meta': {'object_name': 'PendingIndex_ca'},
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
        u'dir.pendingindex_ee': {
            'Meta': {'object_name': 'PendingIndex_ee'},
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
        u'dir.pendingindex_eu': {
            'Meta': {'object_name': 'PendingIndex_eu'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ff': {
            'Meta': {'object_name': 'PendingIndex_ff'},
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
        u'dir.pendingindex_fo': {
            'Meta': {'object_name': 'PendingIndex_fo'},
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
        u'dir.pendingindex_fy': {
            'Meta': {'object_name': 'PendingIndex_fy'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_gl': {
            'Meta': {'object_name': 'PendingIndex_gl'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ha': {
            'Meta': {'object_name': 'PendingIndex_ha'},
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
        u'dir.pendingindex_ig': {
            'Meta': {'object_name': 'PendingIndex_ig'},
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
        u'dir.pendingindex_kg': {
            'Meta': {'object_name': 'PendingIndex_kg'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ki': {
            'Meta': {'object_name': 'PendingIndex_ki'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_lg': {
            'Meta': {'object_name': 'PendingIndex_lg'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ln': {
            'Meta': {'object_name': 'PendingIndex_ln'},
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
        u'dir.pendingindex_nap': {
            'Meta': {'object_name': 'PendingIndex_nap'},
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
        u'dir.pendingindex_nso': {
            'Meta': {'object_name': 'PendingIndex_nso'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ny': {
            'Meta': {'object_name': 'PendingIndex_ny'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_oc': {
            'Meta': {'object_name': 'PendingIndex_oc'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_om': {
            'Meta': {'object_name': 'PendingIndex_om'},
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
        u'dir.pendingindex_pms': {
            'Meta': {'object_name': 'PendingIndex_pms'},
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
        u'dir.pendingindex_rn': {
            'Meta': {'object_name': 'PendingIndex_rn'},
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
        u'dir.pendingindex_rw': {
            'Meta': {'object_name': 'PendingIndex_rw'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_sc': {
            'Meta': {'object_name': 'PendingIndex_sc'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_scn': {
            'Meta': {'object_name': 'PendingIndex_scn'},
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
        u'dir.pendingindex_sn': {
            'Meta': {'object_name': 'PendingIndex_sn'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_so': {
            'Meta': {'object_name': 'PendingIndex_so'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ss': {
            'Meta': {'object_name': 'PendingIndex_ss'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_st': {
            'Meta': {'object_name': 'PendingIndex_st'},
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
        u'dir.pendingindex_tn': {
            'Meta': {'object_name': 'PendingIndex_tn'},
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
        u'dir.pendingindex_ts': {
            'Meta': {'object_name': 'PendingIndex_ts'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_ve': {
            'Meta': {'object_name': 'PendingIndex_ve'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_vec': {
            'Meta': {'object_name': 'PendingIndex_vec'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_wo': {
            'Meta': {'object_name': 'PendingIndex_wo'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_xh': {
            'Meta': {'object_name': 'PendingIndex_xh'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_yo': {
            'Meta': {'object_name': 'PendingIndex_yo'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'})
        },
        u'dir.pendingindex_zu': {
            'Meta': {'object_name': 'PendingIndex_zu'},
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
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ak': {
            'Meta': {'object_name': 'SearchLog_ak'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_bm': {
            'Meta': {'object_name': 'SearchLog_bm'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ca': {
            'Meta': {'object_name': 'SearchLog_ca'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_cs': {
            'Meta': {'object_name': 'SearchLog_cs'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_da': {
            'Meta': {'object_name': 'SearchLog_da'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_de': {
            'Meta': {'object_name': 'SearchLog_de'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ee': {
            'Meta': {'object_name': 'SearchLog_ee'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_el': {
            'Meta': {'object_name': 'SearchLog_el'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_es': {
            'Meta': {'object_name': 'SearchLog_es'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_et': {
            'Meta': {'object_name': 'SearchLog_et'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_eu': {
            'Meta': {'object_name': 'SearchLog_eu'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ff': {
            'Meta': {'object_name': 'SearchLog_ff'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fi': {
            'Meta': {'object_name': 'SearchLog_fi'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fo': {
            'Meta': {'object_name': 'SearchLog_fo'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fr': {
            'Meta': {'object_name': 'SearchLog_fr'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fy': {
            'Meta': {'object_name': 'SearchLog_fy'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_gl': {
            'Meta': {'object_name': 'SearchLog_gl'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ha': {
            'Meta': {'object_name': 'SearchLog_ha'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hr': {
            'Meta': {'object_name': 'SearchLog_hr'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hu': {
            'Meta': {'object_name': 'SearchLog_hu'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ig': {
            'Meta': {'object_name': 'SearchLog_ig'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_is': {
            'Meta': {'object_name': 'SearchLog_is'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_it': {
            'Meta': {'object_name': 'SearchLog_it'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_kg': {
            'Meta': {'object_name': 'SearchLog_kg'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ki': {
            'Meta': {'object_name': 'SearchLog_ki'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lg': {
            'Meta': {'object_name': 'SearchLog_lg'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ln': {
            'Meta': {'object_name': 'SearchLog_ln'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lt': {
            'Meta': {'object_name': 'SearchLog_lt'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lv': {
            'Meta': {'object_name': 'SearchLog_lv'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nap': {
            'Meta': {'object_name': 'SearchLog_nap'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nl': {
            'Meta': {'object_name': 'SearchLog_nl'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_no': {
            'Meta': {'object_name': 'SearchLog_no'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nso': {
            'Meta': {'object_name': 'SearchLog_nso'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ny': {
            'Meta': {'object_name': 'SearchLog_ny'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_oc': {
            'Meta': {'object_name': 'SearchLog_oc'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_om': {
            'Meta': {'object_name': 'SearchLog_om'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pl': {
            'Meta': {'object_name': 'SearchLog_pl'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pms': {
            'Meta': {'object_name': 'SearchLog_pms'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pt': {
            'Meta': {'object_name': 'SearchLog_pt'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_rn': {
            'Meta': {'object_name': 'SearchLog_rn'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ro': {
            'Meta': {'object_name': 'SearchLog_ro'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_rw': {
            'Meta': {'object_name': 'SearchLog_rw'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sc': {
            'Meta': {'object_name': 'SearchLog_sc'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_scn': {
            'Meta': {'object_name': 'SearchLog_scn'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sk': {
            'Meta': {'object_name': 'SearchLog_sk'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sl': {
            'Meta': {'object_name': 'SearchLog_sl'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sn': {
            'Meta': {'object_name': 'SearchLog_sn'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_so': {
            'Meta': {'object_name': 'SearchLog_so'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ss': {
            'Meta': {'object_name': 'SearchLog_ss'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_st': {
            'Meta': {'object_name': 'SearchLog_st'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sv': {
            'Meta': {'object_name': 'SearchLog_sv'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sw': {
            'Meta': {'object_name': 'SearchLog_sw'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_tn': {
            'Meta': {'object_name': 'SearchLog_tn'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_tr': {
            'Meta': {'object_name': 'SearchLog_tr'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ts': {
            'Meta': {'object_name': 'SearchLog_ts'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ve': {
            'Meta': {'object_name': 'SearchLog_ve'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_vec': {
            'Meta': {'object_name': 'SearchLog_vec'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_wo': {
            'Meta': {'object_name': 'SearchLog_wo'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_xh': {
            'Meta': {'object_name': 'SearchLog_xh'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_yo': {
            'Meta': {'object_name': 'SearchLog_yo'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_zu': {
            'Meta': {'object_name': 'SearchLog_zu'},
            'browserstring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
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
        u'dir.siteinfo_ak': {
            'Meta': {'object_name': 'SiteInfo_ak'},
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
        u'dir.siteinfo_bm': {
            'Meta': {'object_name': 'SiteInfo_bm'},
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
        u'dir.siteinfo_ca': {
            'Meta': {'object_name': 'SiteInfo_ca'},
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
        u'dir.siteinfo_ee': {
            'Meta': {'object_name': 'SiteInfo_ee'},
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
        u'dir.siteinfo_eu': {
            'Meta': {'object_name': 'SiteInfo_eu'},
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
        u'dir.siteinfo_ff': {
            'Meta': {'object_name': 'SiteInfo_ff'},
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
        u'dir.siteinfo_fo': {
            'Meta': {'object_name': 'SiteInfo_fo'},
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
        u'dir.siteinfo_fy': {
            'Meta': {'object_name': 'SiteInfo_fy'},
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
        u'dir.siteinfo_gl': {
            'Meta': {'object_name': 'SiteInfo_gl'},
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
        u'dir.siteinfo_ha': {
            'Meta': {'object_name': 'SiteInfo_ha'},
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
        u'dir.siteinfo_ig': {
            'Meta': {'object_name': 'SiteInfo_ig'},
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
        u'dir.siteinfo_kg': {
            'Meta': {'object_name': 'SiteInfo_kg'},
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
        u'dir.siteinfo_ki': {
            'Meta': {'object_name': 'SiteInfo_ki'},
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
        u'dir.siteinfo_lg': {
            'Meta': {'object_name': 'SiteInfo_lg'},
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
        u'dir.siteinfo_ln': {
            'Meta': {'object_name': 'SiteInfo_ln'},
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
        u'dir.siteinfo_nap': {
            'Meta': {'object_name': 'SiteInfo_nap'},
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
        u'dir.siteinfo_nso': {
            'Meta': {'object_name': 'SiteInfo_nso'},
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
        u'dir.siteinfo_ny': {
            'Meta': {'object_name': 'SiteInfo_ny'},
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
        u'dir.siteinfo_oc': {
            'Meta': {'object_name': 'SiteInfo_oc'},
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
        u'dir.siteinfo_om': {
            'Meta': {'object_name': 'SiteInfo_om'},
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
        u'dir.siteinfo_pms': {
            'Meta': {'object_name': 'SiteInfo_pms'},
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
        u'dir.siteinfo_rn': {
            'Meta': {'object_name': 'SiteInfo_rn'},
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
        u'dir.siteinfo_rw': {
            'Meta': {'object_name': 'SiteInfo_rw'},
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
        u'dir.siteinfo_sc': {
            'Meta': {'object_name': 'SiteInfo_sc'},
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
        u'dir.siteinfo_scn': {
            'Meta': {'object_name': 'SiteInfo_scn'},
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
        u'dir.siteinfo_sn': {
            'Meta': {'object_name': 'SiteInfo_sn'},
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
        u'dir.siteinfo_so': {
            'Meta': {'object_name': 'SiteInfo_so'},
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
        u'dir.siteinfo_ss': {
            'Meta': {'object_name': 'SiteInfo_ss'},
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
        u'dir.siteinfo_st': {
            'Meta': {'object_name': 'SiteInfo_st'},
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
        u'dir.siteinfo_tn': {
            'Meta': {'object_name': 'SiteInfo_tn'},
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
        },
        u'dir.siteinfo_ts': {
            'Meta': {'object_name': 'SiteInfo_ts'},
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
        u'dir.siteinfo_ve': {
            'Meta': {'object_name': 'SiteInfo_ve'},
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
        u'dir.siteinfo_vec': {
            'Meta': {'object_name': 'SiteInfo_vec'},
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
        u'dir.siteinfo_wo': {
            'Meta': {'object_name': 'SiteInfo_wo'},
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
        u'dir.siteinfo_xh': {
            'Meta': {'object_name': 'SiteInfo_xh'},
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
        u'dir.siteinfo_yo': {
            'Meta': {'object_name': 'SiteInfo_yo'},
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
        u'dir.siteinfo_zu': {
            'Meta': {'object_name': 'SiteInfo_zu'},
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
