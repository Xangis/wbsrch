# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0006_newssite'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainsearchlog',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_af',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ak',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_bm',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_br',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ca',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_cs',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_cy',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_da',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_de',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ee',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_el',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_eo',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_es',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_et',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_eu',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ff',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_fi',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_fo',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_fr',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_fy',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_gl',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ha',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_hr',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_hu',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ig',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_is',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_it',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_kg',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ki',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_la',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_lg',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ln',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_lt',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_lv',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_nap',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_nl',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_no',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_nso',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ny',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_oc',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_om',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_pl',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_pms',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_pt',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_rn',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ro',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_rw',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sc',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_scn',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sk',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sl',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sn',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_so',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ss',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_st',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sv',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_sw',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_tn',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_tr',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ts',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_ve',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_vec',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_wo',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_xh',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_yo',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchlog_zu',
            name='ip_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
