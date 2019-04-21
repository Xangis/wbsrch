# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0060_auto_20190420_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageiframe',
            name='rooturl_source',
            field=models.CharField(db_index=True, max_length=260, blank=True),
        ),
        migrations.AlterField(
            model_name='pagejavascript',
            name='rooturl_source',
            field=models.CharField(db_index=True, max_length=260, blank=True),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='rooturl_source',
            field=models.CharField(db_index=True, max_length=260, blank=True),
        ),
    ]
