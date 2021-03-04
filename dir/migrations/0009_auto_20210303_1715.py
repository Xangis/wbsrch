# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-04 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0008_auto_20210218_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingindex',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_an',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_ca',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_cs',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_cy',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_da',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_de',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_el',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_es',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_et',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_eu',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_fi',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_fr',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_gl',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_ha',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_hr',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_hu',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_is',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_it',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_lt',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_lv',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_nl',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_no',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_pl',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_pt',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_ro',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_rw',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_sl',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_sn',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_so',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_sv',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_sw',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_tr',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_wo',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_xh',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_yo',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
        migrations.AddField(
            model_name='pendingindex_zu',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], default=2),
        ),
    ]
