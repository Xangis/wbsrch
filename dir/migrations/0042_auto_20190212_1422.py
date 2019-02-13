# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0041_auto_20190212_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelink',
            name='rooturl_destination',
            field=models.CharField(db_index=True, max_length=260, blank=True),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='url_destination',
            field=models.CharField(max_length=2048, blank=True),
        ),
    ]
