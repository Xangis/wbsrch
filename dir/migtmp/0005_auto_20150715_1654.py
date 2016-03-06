# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0004_auto_20150715_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='domains_linking_in',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='domains_linking_in_last_updated',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
