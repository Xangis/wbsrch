# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0030_auto_20160614_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordRanking_ca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(max_length=240, db_index=True)),
                ('rank', models.IntegerField()),
                ('rooturl', models.CharField(db_index=True, max_length=260, blank=True)),
                ('show', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
    ]
