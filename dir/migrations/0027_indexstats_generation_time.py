# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0026_auto_20160501_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexstats',
            name='generation_time',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
