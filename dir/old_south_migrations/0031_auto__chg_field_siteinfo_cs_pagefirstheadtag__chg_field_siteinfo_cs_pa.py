# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SiteInfo_cs.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_cs', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_cs.pagetitle'
        db.alter_column(u'dir_siteinfo_cs', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_cs.rooturl'
        db.alter_column(u'dir_siteinfo_cs', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_cs.pagekeywords'
        db.alter_column(u'dir_siteinfo_cs', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_cs.pagedescription'
        db.alter_column(u'dir_siteinfo_cs', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sw.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sw', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sw.pagetitle'
        db.alter_column(u'dir_siteinfo_sw', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sw.rooturl'
        db.alter_column(u'dir_siteinfo_sw', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_sw.pagekeywords'
        db.alter_column(u'dir_siteinfo_sw', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sw.pagedescription'
        db.alter_column(u'dir_siteinfo_sw', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sv.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sv', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sv.pagetitle'
        db.alter_column(u'dir_siteinfo_sv', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sv.rooturl'
        db.alter_column(u'dir_siteinfo_sv', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_sv.pagekeywords'
        db.alter_column(u'dir_siteinfo_sv', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sv.pagedescription'
        db.alter_column(u'dir_siteinfo_sv', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_si.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_si', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_si.pagetitle'
        db.alter_column(u'dir_siteinfo_si', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_si.rooturl'
        db.alter_column(u'dir_siteinfo_si', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_si.pagekeywords'
        db.alter_column(u'dir_siteinfo_si', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_si.pagedescription'
        db.alter_column(u'dir_siteinfo_si', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sk.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sk', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sk.pagetitle'
        db.alter_column(u'dir_siteinfo_sk', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sk.rooturl'
        db.alter_column(u'dir_siteinfo_sk', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_sk.pagekeywords'
        db.alter_column(u'dir_siteinfo_sk', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_sk.pagedescription'
        db.alter_column(u'dir_siteinfo_sk', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hu.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_hu', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hu.pagetitle'
        db.alter_column(u'dir_siteinfo_hu', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hu.rooturl'
        db.alter_column(u'dir_siteinfo_hu', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_hu.pagekeywords'
        db.alter_column(u'dir_siteinfo_hu', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hu.pagedescription'
        db.alter_column(u'dir_siteinfo_hu', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_hr', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hr.pagetitle'
        db.alter_column(u'dir_siteinfo_hr', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hr.rooturl'
        db.alter_column(u'dir_siteinfo_hr', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_hr.pagekeywords'
        db.alter_column(u'dir_siteinfo_hr', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_hr.pagedescription'
        db.alter_column(u'dir_siteinfo_hr', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_es.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_es', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_es.pagetitle'
        db.alter_column(u'dir_siteinfo_es', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_es.rooturl'
        db.alter_column(u'dir_siteinfo_es', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_es.pagekeywords'
        db.alter_column(u'dir_siteinfo_es', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_es.pagedescription'
        db.alter_column(u'dir_siteinfo_es', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_el.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_el', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_el.pagetitle'
        db.alter_column(u'dir_siteinfo_el', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_el.rooturl'
        db.alter_column(u'dir_siteinfo_el', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_el.pagekeywords'
        db.alter_column(u'dir_siteinfo_el', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_el.pagedescription'
        db.alter_column(u'dir_siteinfo_el', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_ro.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_ro', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_ro.pagetitle'
        db.alter_column(u'dir_siteinfo_ro', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_ro.rooturl'
        db.alter_column(u'dir_siteinfo_ro', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_ro.pagekeywords'
        db.alter_column(u'dir_siteinfo_ro', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_ro.pagedescription'
        db.alter_column(u'dir_siteinfo_ro', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_da.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_da', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_da.pagetitle'
        db.alter_column(u'dir_siteinfo_da', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_da.rooturl'
        db.alter_column(u'dir_siteinfo_da', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_da.pagekeywords'
        db.alter_column(u'dir_siteinfo_da', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_da.pagedescription'
        db.alter_column(u'dir_siteinfo_da', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_et.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_et', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_et.pagetitle'
        db.alter_column(u'dir_siteinfo_et', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_et.rooturl'
        db.alter_column(u'dir_siteinfo_et', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_et.pagekeywords'
        db.alter_column(u'dir_siteinfo_et', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_et.pagedescription'
        db.alter_column(u'dir_siteinfo_et', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_de.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_de', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_de.pagetitle'
        db.alter_column(u'dir_siteinfo_de', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_de.rooturl'
        db.alter_column(u'dir_siteinfo_de', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_de.pagekeywords'
        db.alter_column(u'dir_siteinfo_de', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_de.pagedescription'
        db.alter_column(u'dir_siteinfo_de', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lt.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_lt', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lt.pagetitle'
        db.alter_column(u'dir_siteinfo_lt', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lt.rooturl'
        db.alter_column(u'dir_siteinfo_lt', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_lt.pagekeywords'
        db.alter_column(u'dir_siteinfo_lt', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lt.pagedescription'
        db.alter_column(u'dir_siteinfo_lt', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lv.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_lv', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lv.pagetitle'
        db.alter_column(u'dir_siteinfo_lv', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lv.rooturl'
        db.alter_column(u'dir_siteinfo_lv', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_lv.pagekeywords'
        db.alter_column(u'dir_siteinfo_lv', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_lv.pagedescription'
        db.alter_column(u'dir_siteinfo_lv', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_tr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_tr', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_tr.pagetitle'
        db.alter_column(u'dir_siteinfo_tr', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_tr.rooturl'
        db.alter_column(u'dir_siteinfo_tr', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_tr.pagekeywords'
        db.alter_column(u'dir_siteinfo_tr', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_tr.pagedescription'
        db.alter_column(u'dir_siteinfo_tr', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pt.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_pt', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pt.pagetitle'
        db.alter_column(u'dir_siteinfo_pt', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pt.rooturl'
        db.alter_column(u'dir_siteinfo_pt', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_pt.pagekeywords'
        db.alter_column(u'dir_siteinfo_pt', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pt.pagedescription'
        db.alter_column(u'dir_siteinfo_pt', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pl.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_pl', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pl.pagetitle'
        db.alter_column(u'dir_siteinfo_pl', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pl.rooturl'
        db.alter_column(u'dir_siteinfo_pl', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_pl.pagekeywords'
        db.alter_column(u'dir_siteinfo_pl', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_pl.pagedescription'
        db.alter_column(u'dir_siteinfo_pl', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_it.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_it', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_it.pagetitle'
        db.alter_column(u'dir_siteinfo_it', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_it.rooturl'
        db.alter_column(u'dir_siteinfo_it', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_it.pagekeywords'
        db.alter_column(u'dir_siteinfo_it', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_it.pagedescription'
        db.alter_column(u'dir_siteinfo_it', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_is.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_is', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_is.pagetitle'
        db.alter_column(u'dir_siteinfo_is', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_is.rooturl'
        db.alter_column(u'dir_siteinfo_is', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_is.pagekeywords'
        db.alter_column(u'dir_siteinfo_is', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_is.pagedescription'
        db.alter_column(u'dir_siteinfo_is', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_fr', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fr.pagetitle'
        db.alter_column(u'dir_siteinfo_fr', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fr.rooturl'
        db.alter_column(u'dir_siteinfo_fr', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_fr.pagekeywords'
        db.alter_column(u'dir_siteinfo_fr', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fr.pagedescription'
        db.alter_column(u'dir_siteinfo_fr', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_no.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_no', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_no.pagetitle'
        db.alter_column(u'dir_siteinfo_no', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_no.rooturl'
        db.alter_column(u'dir_siteinfo_no', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_no.pagekeywords'
        db.alter_column(u'dir_siteinfo_no', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_no.pagedescription'
        db.alter_column(u'dir_siteinfo_no', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_nl.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_nl', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_nl.pagetitle'
        db.alter_column(u'dir_siteinfo_nl', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_nl.rooturl'
        db.alter_column(u'dir_siteinfo_nl', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_nl.pagekeywords'
        db.alter_column(u'dir_siteinfo_nl', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_nl.pagedescription'
        db.alter_column(u'dir_siteinfo_nl', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fi.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_fi', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fi.pagetitle'
        db.alter_column(u'dir_siteinfo_fi', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fi.rooturl'
        db.alter_column(u'dir_siteinfo_fi', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo_fi.pagekeywords'
        db.alter_column(u'dir_siteinfo_fi', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo_fi.pagedescription'
        db.alter_column(u'dir_siteinfo_fi', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

        # Changing field 'SiteInfo.pagefirstheadtag'
        db.alter_column(u'site_info', 'pagefirstheadtag', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo.pagetitle'
        db.alter_column(u'site_info', 'pagetitle', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo.rooturl'
        db.alter_column(u'site_info', 'rooturl', self.gf('django.db.models.fields.CharField')(max_length=260))

        # Changing field 'SiteInfo.pagekeywords'
        db.alter_column(u'site_info', 'pagekeywords', self.gf('django.db.models.fields.CharField')(max_length=260, null=True))

        # Changing field 'SiteInfo.pagedescription'
        db.alter_column(u'site_info', 'pagedescription', self.gf('django.db.models.fields.TextField')(max_length=260, null=True))

    def backwards(self, orm):

        # Changing field 'SiteInfo_cs.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_cs', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_cs.pagetitle'
        db.alter_column(u'dir_siteinfo_cs', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_cs.rooturl'
        db.alter_column(u'dir_siteinfo_cs', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_cs.pagekeywords'
        db.alter_column(u'dir_siteinfo_cs', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_cs.pagedescription'
        db.alter_column(u'dir_siteinfo_cs', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sw.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sw', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sw.pagetitle'
        db.alter_column(u'dir_siteinfo_sw', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sw.rooturl'
        db.alter_column(u'dir_siteinfo_sw', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_sw.pagekeywords'
        db.alter_column(u'dir_siteinfo_sw', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sw.pagedescription'
        db.alter_column(u'dir_siteinfo_sw', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sv.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sv', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sv.pagetitle'
        db.alter_column(u'dir_siteinfo_sv', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sv.rooturl'
        db.alter_column(u'dir_siteinfo_sv', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_sv.pagekeywords'
        db.alter_column(u'dir_siteinfo_sv', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sv.pagedescription'
        db.alter_column(u'dir_siteinfo_sv', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_si.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_si', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_si.pagetitle'
        db.alter_column(u'dir_siteinfo_si', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_si.rooturl'
        db.alter_column(u'dir_siteinfo_si', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_si.pagekeywords'
        db.alter_column(u'dir_siteinfo_si', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_si.pagedescription'
        db.alter_column(u'dir_siteinfo_si', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sk.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_sk', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sk.pagetitle'
        db.alter_column(u'dir_siteinfo_sk', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sk.rooturl'
        db.alter_column(u'dir_siteinfo_sk', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_sk.pagekeywords'
        db.alter_column(u'dir_siteinfo_sk', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_sk.pagedescription'
        db.alter_column(u'dir_siteinfo_sk', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hu.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_hu', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hu.pagetitle'
        db.alter_column(u'dir_siteinfo_hu', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hu.rooturl'
        db.alter_column(u'dir_siteinfo_hu', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_hu.pagekeywords'
        db.alter_column(u'dir_siteinfo_hu', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hu.pagedescription'
        db.alter_column(u'dir_siteinfo_hu', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_hr', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hr.pagetitle'
        db.alter_column(u'dir_siteinfo_hr', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hr.rooturl'
        db.alter_column(u'dir_siteinfo_hr', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_hr.pagekeywords'
        db.alter_column(u'dir_siteinfo_hr', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_hr.pagedescription'
        db.alter_column(u'dir_siteinfo_hr', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_es.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_es', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_es.pagetitle'
        db.alter_column(u'dir_siteinfo_es', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_es.rooturl'
        db.alter_column(u'dir_siteinfo_es', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_es.pagekeywords'
        db.alter_column(u'dir_siteinfo_es', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_es.pagedescription'
        db.alter_column(u'dir_siteinfo_es', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_el.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_el', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_el.pagetitle'
        db.alter_column(u'dir_siteinfo_el', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_el.rooturl'
        db.alter_column(u'dir_siteinfo_el', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_el.pagekeywords'
        db.alter_column(u'dir_siteinfo_el', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_el.pagedescription'
        db.alter_column(u'dir_siteinfo_el', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_ro.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_ro', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_ro.pagetitle'
        db.alter_column(u'dir_siteinfo_ro', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_ro.rooturl'
        db.alter_column(u'dir_siteinfo_ro', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_ro.pagekeywords'
        db.alter_column(u'dir_siteinfo_ro', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_ro.pagedescription'
        db.alter_column(u'dir_siteinfo_ro', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_da.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_da', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_da.pagetitle'
        db.alter_column(u'dir_siteinfo_da', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_da.rooturl'
        db.alter_column(u'dir_siteinfo_da', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_da.pagekeywords'
        db.alter_column(u'dir_siteinfo_da', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_da.pagedescription'
        db.alter_column(u'dir_siteinfo_da', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_et.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_et', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_et.pagetitle'
        db.alter_column(u'dir_siteinfo_et', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_et.rooturl'
        db.alter_column(u'dir_siteinfo_et', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_et.pagekeywords'
        db.alter_column(u'dir_siteinfo_et', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_et.pagedescription'
        db.alter_column(u'dir_siteinfo_et', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_de.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_de', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_de.pagetitle'
        db.alter_column(u'dir_siteinfo_de', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_de.rooturl'
        db.alter_column(u'dir_siteinfo_de', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_de.pagekeywords'
        db.alter_column(u'dir_siteinfo_de', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_de.pagedescription'
        db.alter_column(u'dir_siteinfo_de', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lt.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_lt', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lt.pagetitle'
        db.alter_column(u'dir_siteinfo_lt', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lt.rooturl'
        db.alter_column(u'dir_siteinfo_lt', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_lt.pagekeywords'
        db.alter_column(u'dir_siteinfo_lt', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lt.pagedescription'
        db.alter_column(u'dir_siteinfo_lt', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lv.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_lv', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lv.pagetitle'
        db.alter_column(u'dir_siteinfo_lv', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lv.rooturl'
        db.alter_column(u'dir_siteinfo_lv', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_lv.pagekeywords'
        db.alter_column(u'dir_siteinfo_lv', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_lv.pagedescription'
        db.alter_column(u'dir_siteinfo_lv', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_tr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_tr', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_tr.pagetitle'
        db.alter_column(u'dir_siteinfo_tr', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_tr.rooturl'
        db.alter_column(u'dir_siteinfo_tr', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_tr.pagekeywords'
        db.alter_column(u'dir_siteinfo_tr', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_tr.pagedescription'
        db.alter_column(u'dir_siteinfo_tr', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pt.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_pt', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pt.pagetitle'
        db.alter_column(u'dir_siteinfo_pt', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pt.rooturl'
        db.alter_column(u'dir_siteinfo_pt', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_pt.pagekeywords'
        db.alter_column(u'dir_siteinfo_pt', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pt.pagedescription'
        db.alter_column(u'dir_siteinfo_pt', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pl.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_pl', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pl.pagetitle'
        db.alter_column(u'dir_siteinfo_pl', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pl.rooturl'
        db.alter_column(u'dir_siteinfo_pl', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_pl.pagekeywords'
        db.alter_column(u'dir_siteinfo_pl', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_pl.pagedescription'
        db.alter_column(u'dir_siteinfo_pl', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_it.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_it', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_it.pagetitle'
        db.alter_column(u'dir_siteinfo_it', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_it.rooturl'
        db.alter_column(u'dir_siteinfo_it', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_it.pagekeywords'
        db.alter_column(u'dir_siteinfo_it', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_it.pagedescription'
        db.alter_column(u'dir_siteinfo_it', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_is.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_is', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_is.pagetitle'
        db.alter_column(u'dir_siteinfo_is', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_is.rooturl'
        db.alter_column(u'dir_siteinfo_is', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_is.pagekeywords'
        db.alter_column(u'dir_siteinfo_is', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_is.pagedescription'
        db.alter_column(u'dir_siteinfo_is', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fr.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_fr', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fr.pagetitle'
        db.alter_column(u'dir_siteinfo_fr', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fr.rooturl'
        db.alter_column(u'dir_siteinfo_fr', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_fr.pagekeywords'
        db.alter_column(u'dir_siteinfo_fr', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fr.pagedescription'
        db.alter_column(u'dir_siteinfo_fr', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_no.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_no', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_no.pagetitle'
        db.alter_column(u'dir_siteinfo_no', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_no.rooturl'
        db.alter_column(u'dir_siteinfo_no', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_no.pagekeywords'
        db.alter_column(u'dir_siteinfo_no', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_no.pagedescription'
        db.alter_column(u'dir_siteinfo_no', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_nl.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_nl', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_nl.pagetitle'
        db.alter_column(u'dir_siteinfo_nl', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_nl.rooturl'
        db.alter_column(u'dir_siteinfo_nl', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_nl.pagekeywords'
        db.alter_column(u'dir_siteinfo_nl', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_nl.pagedescription'
        db.alter_column(u'dir_siteinfo_nl', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fi.pagefirstheadtag'
        db.alter_column(u'dir_siteinfo_fi', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fi.pagetitle'
        db.alter_column(u'dir_siteinfo_fi', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fi.rooturl'
        db.alter_column(u'dir_siteinfo_fi', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo_fi.pagekeywords'
        db.alter_column(u'dir_siteinfo_fi', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo_fi.pagedescription'
        db.alter_column(u'dir_siteinfo_fi', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo.pagefirstheadtag'
        db.alter_column(u'site_info', 'pagefirstheadtag', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo.pagetitle'
        db.alter_column(u'site_info', 'pagetitle', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo.rooturl'
        db.alter_column(u'site_info', 'rooturl', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SiteInfo.pagekeywords'
        db.alter_column(u'site_info', 'pagekeywords', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SiteInfo.pagedescription'
        db.alter_column(u'site_info', 'pagedescription', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'dir.domaininfo': {
            'Meta': {'object_name': 'DomainInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_association': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rank_adjustment': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rank_reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_cs': {
            'Meta': {'object_name': 'IndexTerm_cs'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_da': {
            'Meta': {'object_name': 'IndexTerm_da'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_de': {
            'Meta': {'object_name': 'IndexTerm_de'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_el': {
            'Meta': {'object_name': 'IndexTerm_el'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_es': {
            'Meta': {'object_name': 'IndexTerm_es'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_et': {
            'Meta': {'object_name': 'IndexTerm_et'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fi': {
            'Meta': {'object_name': 'IndexTerm_fi'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_fr': {
            'Meta': {'object_name': 'IndexTerm_fr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_hr': {
            'Meta': {'object_name': 'IndexTerm_hr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_hu': {
            'Meta': {'object_name': 'IndexTerm_hu'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_is': {
            'Meta': {'object_name': 'IndexTerm_is'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_it': {
            'Meta': {'object_name': 'IndexTerm_it'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_lt': {
            'Meta': {'object_name': 'IndexTerm_lt'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_lv': {
            'Meta': {'object_name': 'IndexTerm_lv'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_nl': {
            'Meta': {'object_name': 'IndexTerm_nl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_no': {
            'Meta': {'object_name': 'IndexTerm_no'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pl': {
            'Meta': {'object_name': 'IndexTerm_pl'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_pt': {
            'Meta': {'object_name': 'IndexTerm_pt'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_ro': {
            'Meta': {'object_name': 'IndexTerm_ro'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_si': {
            'Meta': {'object_name': 'IndexTerm_si'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sk': {
            'Meta': {'object_name': 'IndexTerm_sk'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sv': {
            'Meta': {'object_name': 'IndexTerm_sv'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_sw': {
            'Meta': {'object_name': 'IndexTerm_sw'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'num_results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_rankings': ('django.db.models.fields.TextField', [], {})
        },
        u'dir.indexterm_tr': {
            'Meta': {'object_name': 'IndexTerm_tr'},
            'date_indexed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
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
        u'dir.pendingindex_si': {
            'Meta': {'object_name': 'PendingIndex_si'},
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
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_cs': {
            'Meta': {'object_name': 'SearchLog_cs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_da': {
            'Meta': {'object_name': 'SearchLog_da'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_de': {
            'Meta': {'object_name': 'SearchLog_de'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_el': {
            'Meta': {'object_name': 'SearchLog_el'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_es': {
            'Meta': {'object_name': 'SearchLog_es'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_et': {
            'Meta': {'object_name': 'SearchLog_et'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fi': {
            'Meta': {'object_name': 'SearchLog_fi'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_fr': {
            'Meta': {'object_name': 'SearchLog_fr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hr': {
            'Meta': {'object_name': 'SearchLog_hr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_hu': {
            'Meta': {'object_name': 'SearchLog_hu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_is': {
            'Meta': {'object_name': 'SearchLog_is'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_it': {
            'Meta': {'object_name': 'SearchLog_it'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lt': {
            'Meta': {'object_name': 'SearchLog_lt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_lv': {
            'Meta': {'object_name': 'SearchLog_lv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_nl': {
            'Meta': {'object_name': 'SearchLog_nl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_no': {
            'Meta': {'object_name': 'SearchLog_no'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pl': {
            'Meta': {'object_name': 'SearchLog_pl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_pt': {
            'Meta': {'object_name': 'SearchLog_pt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_ro': {
            'Meta': {'object_name': 'SearchLog_ro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_si': {
            'Meta': {'object_name': 'SearchLog_si'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sk': {
            'Meta': {'object_name': 'SearchLog_sk'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sv': {
            'Meta': {'object_name': 'SearchLog_sv'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_sw': {
            'Meta': {'object_name': 'SearchLog_sw'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'last_search': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_count': ('django.db.models.fields.IntegerField', [], {}),
            'search_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        u'dir.searchlog_tr': {
            'Meta': {'object_name': 'SearchLog_tr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_cs': {
            'Meta': {'object_name': 'SiteInfo_cs'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_da': {
            'Meta': {'object_name': 'SiteInfo_da'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_de': {
            'Meta': {'object_name': 'SiteInfo_de'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_el': {
            'Meta': {'object_name': 'SiteInfo_el'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_es': {
            'Meta': {'object_name': 'SiteInfo_es'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_et': {
            'Meta': {'object_name': 'SiteInfo_et'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_fi': {
            'Meta': {'object_name': 'SiteInfo_fi'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_fr': {
            'Meta': {'object_name': 'SiteInfo_fr'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_hr': {
            'Meta': {'object_name': 'SiteInfo_hr'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_hu': {
            'Meta': {'object_name': 'SiteInfo_hu'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_is': {
            'Meta': {'object_name': 'SiteInfo_is'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_it': {
            'Meta': {'object_name': 'SiteInfo_it'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_lt': {
            'Meta': {'object_name': 'SiteInfo_lt'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_lv': {
            'Meta': {'object_name': 'SiteInfo_lv'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_nl': {
            'Meta': {'object_name': 'SiteInfo_nl'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_no': {
            'Meta': {'object_name': 'SiteInfo_no'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_pl': {
            'Meta': {'object_name': 'SiteInfo_pl'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_pt': {
            'Meta': {'object_name': 'SiteInfo_pt'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_ro': {
            'Meta': {'object_name': 'SiteInfo_ro'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_si': {
            'Meta': {'object_name': 'SiteInfo_si'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_sk': {
            'Meta': {'object_name': 'SiteInfo_sk'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_sv': {
            'Meta': {'object_name': 'SiteInfo_sv'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_sw': {
            'Meta': {'object_name': 'SiteInfo_sw'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'dir.siteinfo_tr': {
            'Meta': {'object_name': 'SiteInfo_tr'},
            'firstcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastcrawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagedescription': ('django.db.models.fields.TextField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagefirstheadtag': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagekeywords': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'pagesize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pagetext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'rooturl': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dir']