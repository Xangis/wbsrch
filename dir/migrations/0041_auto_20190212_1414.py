# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0040_auto_20190123_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelink',
            name='url_destination',
            field=models.CharField(db_index=True, max_length=2048, blank=True),
        ),
    ]
