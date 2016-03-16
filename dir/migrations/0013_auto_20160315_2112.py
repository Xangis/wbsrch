# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0012_domaininfo_domain_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_state',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
