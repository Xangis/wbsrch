# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0009_auto_20160227_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfoEndingInEDU',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Site Infos Ending With .edu',
            },
            bases=('dir.siteinfo',),
        ),
        migrations.RenameField(
            model_name='domaininfo',
            old_name='expiration_last_updated',
            new_name='whois_last_updated',
        ),
    ]
