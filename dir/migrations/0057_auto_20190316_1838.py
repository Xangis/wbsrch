# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0056_auto_20190316_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_name',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_org',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
