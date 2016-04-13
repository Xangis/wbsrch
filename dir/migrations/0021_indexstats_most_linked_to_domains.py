# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0020_auto_20160409_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexstats',
            name='most_linked_to_domains',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
