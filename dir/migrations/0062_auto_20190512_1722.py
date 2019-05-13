# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0061_auto_20190421_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainsuffix',
            name='no_new_domain_urls',
        ),
        migrations.AddField(
            model_name='domainsuffix',
            name='blocked_to_crawled_ratio',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domainsuffix',
            name='num_blocked',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domainsuffix',
            name='num_crawled',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domainsuffix',
            name='num_known',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='domainsuffix',
            name='extension',
            field=models.CharField(max_length=24, db_index=True),
        ),
    ]
