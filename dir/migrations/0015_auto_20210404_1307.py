# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-04 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0014_autocomplete_sk_indexterm_sk_keywordranking_sk_pendingindex_sk_siteinfo_sk'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResultClick_sk',
        ),
        migrations.DeleteModel(
            name='SearchLog_sk',
        ),
    ]