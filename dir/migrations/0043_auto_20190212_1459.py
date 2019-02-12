# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0042_auto_20190212_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='alexa_outdated',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
