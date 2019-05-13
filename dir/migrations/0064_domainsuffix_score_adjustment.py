# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0063_domainsuffix_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainsuffix',
            name='score_adjustment',
            field=models.IntegerField(default=0),
        ),
    ]
