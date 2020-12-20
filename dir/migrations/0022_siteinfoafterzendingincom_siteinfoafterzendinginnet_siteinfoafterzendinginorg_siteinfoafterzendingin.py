# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0021_indexstats_most_linked_to_domains'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfoAfterZEndingInCOM',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Site Infos After Z ending in COM',
            },
            bases=('dir.siteinfo',),
        ),
        migrations.CreateModel(
            name='SiteInfoAfterZEndingInNET',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Site Infos After Z ending in NET',
            },
            bases=('dir.siteinfo',),
        ),
        migrations.CreateModel(
            name='SiteInfoAfterZEndingInORG',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Site Infos After Z ending in ORG',
            },
            bases=('dir.siteinfo',),
        ),
        migrations.CreateModel(
            name='SiteInfoAfterZEndingInUS',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Site Infos After Z ending in US',
            },
            bases=('dir.siteinfo',),
        ),
    ]
