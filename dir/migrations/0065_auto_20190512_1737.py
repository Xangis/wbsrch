# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0064_domainsuffix_score_adjustment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainsuffix',
            name='blocked_to_crawled_ratio',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
    ]
