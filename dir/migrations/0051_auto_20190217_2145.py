# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0050_auto_20190217_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favicon',
            name='icon',
            field=models.TextField(),
        ),
    ]
