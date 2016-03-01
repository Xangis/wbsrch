# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainSearchLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('result_count', models.IntegerField()),
                ('last_search', models.DateTimeField(auto_now_add=True)),
                ('search_time', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('indexed', models.BooleanField(default=False)),
                ('referer', models.CharField(max_length=255, null=True, blank=True)),
                ('ip', models.CharField(max_length=16, null=True, blank=True)),
                ('browserstring', models.CharField(max_length=255, null=True, blank=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('language', models.CharField(max_length=6)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
            bases=(models.Model,),
        ),
    ]
