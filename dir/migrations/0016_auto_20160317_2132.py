# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0015_auto_20160316_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_zipcode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
