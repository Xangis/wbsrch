# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0005_indexterm_br_keywordranking_br_pendingindex_br_searchlog_br_siteinfo_br'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(db_index=True, max_length=260, blank=True)),
            ],
            options={
                'in_db': 'urls',
            },
        ),
    ]
