# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-15 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0002_domaininfo_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
