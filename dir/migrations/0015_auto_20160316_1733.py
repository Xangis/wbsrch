# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0014_auto_20160315_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='whois_emails',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_nameservers',
            field=models.TextField(null=True, blank=True),
        ),
    ]
