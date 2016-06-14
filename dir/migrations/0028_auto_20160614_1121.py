# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0027_indexstats_generation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexstats',
            name='last_most_linked_to',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blockedsite',
            name='reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='rank_reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
    ]
