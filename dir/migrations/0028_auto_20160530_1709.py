# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0027_indexstats_generation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_af',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ak',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_bm',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_br',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ca',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_cs',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_cy',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_da',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_de',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ee',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_el',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_eo',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_es',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_et',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_eu',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ff',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_fi',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_fo',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_fr',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_fy',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_gl',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ha',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_hr',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_hu',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ig',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_is',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_it',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_kg',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ki',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_la',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_lg',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ln',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_lt',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_lv',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_nap',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_nl',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_no',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_nso',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ny',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_oc',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_om',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_pl',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_pms',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_pt',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_rn',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ro',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_rw',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sc',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_scn',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sk',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sl',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sn',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_so',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ss',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_st',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sv',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_sw',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_tn',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_tr',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ts',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_ve',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_vec',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_wo',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_xh',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_yo',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo_zu',
            name='simhash_value',
            field=models.CharField(db_index=True, max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blockedsite',
            name='reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='rank_reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
    ]
