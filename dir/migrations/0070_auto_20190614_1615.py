# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0069_apitoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainsuffix',
            name='extension',
            field=models.CharField(max_length=30, db_index=True),
        ),
    ]
