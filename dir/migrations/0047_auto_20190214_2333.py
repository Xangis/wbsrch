# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0046_auto_20190214_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='file_large',
            field=models.FileField(help_text=b'1280x800px image file location.', null=True, upload_to=b'../screenshots', blank=True),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='file_small',
            field=models.FileField(help_text=b'320x200px image file location.', null=True, upload_to=b'../screenshots', blank=True),
        ),
    ]
