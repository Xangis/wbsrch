# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0051_auto_20190217_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='favicon',
            name='format',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
