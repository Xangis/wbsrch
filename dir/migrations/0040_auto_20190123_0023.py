# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0039_auto_20190109_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedsite',
            name='reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language - Unspecified'), (37, b'Unindexed Language - Albanian'), (20, b'Unindexed Language - Arabic or Farsi'), (32, b'Unindexed Language - Armenian'), (34, b'Unindexed Language - Azerbaijani'), (21, b'Unindexed Language - Chinese'), (31, b'Unindexed Language - Georgian'), (22, b'Unindexed Language - Hebrew'), (23, b'Unindexed Language - Hindi'), (24, b'Unindexed Language - Indonesian or Similar'), (25, b'Unindexed Language - Japanese'), (26, b'Unindexed Language - Khmer'), (27, b'Unindexed Language - Korean'), (41, b'Unindexed Language - Macedonian'), (39, b'Unindexed Language - Punjabi'), (40, b'Unindexed Language - Pashto'), (28, b'Unindexed Language - Russian or Other Cyrillic'), (33, b'Unindexed Language - Serbian'), (36, b'Unindexed Language - Sinhala'), (38, b'Unindexed Language - Tagalog'), (42, b'Unindexed Language - Telugu'), (30, b'Unindexed Language - Thai'), (35, b'Unindexed Language - Urdu'), (29, b'Unindexed Language - Vietnamese'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='rank_reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language - Unspecified'), (37, b'Unindexed Language - Albanian'), (20, b'Unindexed Language - Arabic or Farsi'), (32, b'Unindexed Language - Armenian'), (34, b'Unindexed Language - Azerbaijani'), (21, b'Unindexed Language - Chinese'), (31, b'Unindexed Language - Georgian'), (22, b'Unindexed Language - Hebrew'), (23, b'Unindexed Language - Hindi'), (24, b'Unindexed Language - Indonesian or Similar'), (25, b'Unindexed Language - Japanese'), (26, b'Unindexed Language - Khmer'), (27, b'Unindexed Language - Korean'), (41, b'Unindexed Language - Macedonian'), (39, b'Unindexed Language - Punjabi'), (40, b'Unindexed Language - Pashto'), (28, b'Unindexed Language - Russian or Other Cyrillic'), (33, b'Unindexed Language - Serbian'), (36, b'Unindexed Language - Sinhala'), (38, b'Unindexed Language - Tagalog'), (42, b'Unindexed Language - Telugu'), (30, b'Unindexed Language - Thai'), (35, b'Unindexed Language - Urdu'), (29, b'Unindexed Language - Vietnamese'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
    ]
