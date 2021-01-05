# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-26 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0071_apiuser_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=80)),
                ('count', models.IntegerField()),
                ('version', models.DecimalField(decimal_places=4, max_digits=8)),
                ('enabled', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]