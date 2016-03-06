# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0006_auto_20150715_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parameter', models.CharField(max_length=60)),
                ('domain', models.CharField(db_index=True, max_length=260, blank=True)),
                ('replace_with', models.CharField(help_text=b'What should the parameter contents be replaced with? If blank, the tag will be removed.', max_length=100, null=True, blank=True)),
                ('remove_before_crawl', models.BooleanField(default=False, help_text=b'Should this parameter be removed before crawling?')),
                ('replace_before_crawl', models.BooleanField(default=False, help_text=b'Should this parameter be replaced before crawling?')),
                ('remove_or_replace_after_crawl', models.BooleanField(default=True, help_text=b'Should this parameter be removed or replaced after crawling?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
