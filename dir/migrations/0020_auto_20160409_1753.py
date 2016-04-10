# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0019_apisubscription_apiusage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_country',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
