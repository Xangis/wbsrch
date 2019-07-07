# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0070_auto_20190614_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiuser',
            name='userid',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
