# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0036_autocomplete_sw_indexterm_sw_keywordranking_sw_pendingindex_sw_siteinfo_sw'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockedsite',
            name='date_added',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 0, 0), auto_now_add=True, db_index=True),
            preserve_default=False,
        ),
    ]
