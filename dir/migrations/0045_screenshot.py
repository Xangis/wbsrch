# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0044_auto_20190212_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_large', models.FileField(help_text=b'1280x800px image file location.', null=True, upload_to=b'', blank=True)),
                ('file_small', models.FileField(help_text=b'320x200px image file location.', null=True, upload_to=b'', blank=True)),
                ('date_taken', models.DateField(auto_now_add=True)),
                ('domain', models.ForeignKey(to='dir.DomainInfo')),
            ],
        ),
    ]
