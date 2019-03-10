# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0053_auto_20190307_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='majestic_outdated',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='majestic_rank',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='majestic_rank_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
