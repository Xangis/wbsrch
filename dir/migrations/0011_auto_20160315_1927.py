# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0010_auto_20160315_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='whois_address',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_city',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_country',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_org',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_registrar',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_state',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='whois_zipcode',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
