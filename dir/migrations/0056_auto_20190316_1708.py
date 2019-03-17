# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0055_auto_20190316_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_state',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_zipcode',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
