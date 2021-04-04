# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-04 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0015_auto_20210404_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultClick_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField()),
                ('search_id', models.UUIDField(db_index=True, editable=False, null=True)),
                ('position', models.IntegerField()),
                ('ip', models.CharField(blank=True, max_length=16, null=True)),
                ('url', models.TextField(db_index=True)),
                ('click_time', models.DateTimeField(auto_now_add=True)),
                ('xpos', models.IntegerField(blank=True, null=True)),
                ('ypos', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchLog_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(db_index=True)),
                ('result_count', models.IntegerField()),
                ('last_search', models.DateTimeField(auto_now_add=True)),
                ('search_time', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('indexed', models.BooleanField(default=False)),
                ('referer', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=16, null=True)),
                ('ip_country', models.CharField(blank=True, max_length=3, null=True)),
                ('browserstring', models.CharField(blank=True, max_length=255, null=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('search_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, null=True)),
            ],
        ),
    ]
