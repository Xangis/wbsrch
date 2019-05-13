# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0062_auto_20190512_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainsuffix',
            name='last_updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
