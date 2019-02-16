# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0047_auto_20190214_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='file_large',
            field=models.TextField(help_text=b'1280x800px image file location.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='file_small',
            field=models.TextField(help_text=b'320x200px image file location.', null=True, blank=True),
        ),
    ]
