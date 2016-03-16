# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0013_auto_20160315_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_address',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
