# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0054_auto_20190309_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedsite',
            name='reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language - Unspecified'), (37, b'Unindexed Language - Albanian'), (45, b'Unindexed Language - Amharic'), (20, b'Unindexed Language - Arabic or Farsi'), (32, b'Unindexed Language - Armenian'), (50, b'Unindexed Language - Assamese'), (34, b'Unindexed Language - Azerbaijani'), (59, b'Unindexed Language - Belarusian'), (60, b'Unindexed Language - Bangladeshi'), (21, b'Unindexed Language - Chinese'), (56, b'Unindexed Language - Dzongkha'), (31, b'Unindexed Language - Georgian'), (46, b'Unindexed Language - Gujarati'), (22, b'Unindexed Language - Hebrew'), (23, b'Unindexed Language - Hindi'), (24, b'Unindexed Language - Indonesian or Similar'), (25, b'Unindexed Language - Japanese'), (49, b'Unindexed Language - Javanese'), (58, b'Unindexed Language - Kannada'), (43, b'Unindexed Language - Kazakh'), (26, b'Unindexed Language - Khmer'), (27, b'Unindexed Language - Korean'), (44, b'Unindexed Language - Kyrgyz'), (47, b'Unindexed Language - Kurdish'), (54, b'Unindexed Language - Lao'), (41, b'Unindexed Language - Macedonian'), (55, b'Unindexed Language - Marathi'), (48, b'Unindexed Language - Mongolian'), (52, b'Unindexed Language - Nepali'), (57, b'Unindexed Language - Oriya'), (39, b'Unindexed Language - Punjabi'), (40, b'Unindexed Language - Pashto'), (28, b'Unindexed Language - Russian or Other Cyrillic'), (33, b'Unindexed Language - Serbian'), (36, b'Unindexed Language - Sinhala'), (38, b'Unindexed Language - Tagalog'), (51, b'Unindexed Language - Tamil'), (42, b'Unindexed Language - Telugu'), (30, b'Unindexed Language - Thai'), (53, b'Unindexed Language - Uighur'), (35, b'Unindexed Language - Urdu'), (29, b'Unindexed Language - Vietnamese'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='rank_reason',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Content Farm'), (1, b'Aggregator or Meta Site'), (2, b'Social'), (3, b'Bait and Switch'), (4, b'Porn or Adult Content'), (5, b'Pills'), (6, b'Online Gambling'), (7, b'Spam or Computer Generated Content'), (8, b'Unindexed Language - Unspecified'), (37, b'Unindexed Language - Albanian'), (45, b'Unindexed Language - Amharic'), (20, b'Unindexed Language - Arabic or Farsi'), (32, b'Unindexed Language - Armenian'), (50, b'Unindexed Language - Assamese'), (34, b'Unindexed Language - Azerbaijani'), (59, b'Unindexed Language - Belarusian'), (60, b'Unindexed Language - Bangladeshi'), (21, b'Unindexed Language - Chinese'), (56, b'Unindexed Language - Dzongkha'), (31, b'Unindexed Language - Georgian'), (46, b'Unindexed Language - Gujarati'), (22, b'Unindexed Language - Hebrew'), (23, b'Unindexed Language - Hindi'), (24, b'Unindexed Language - Indonesian or Similar'), (25, b'Unindexed Language - Japanese'), (49, b'Unindexed Language - Javanese'), (58, b'Unindexed Language - Kannada'), (43, b'Unindexed Language - Kazakh'), (26, b'Unindexed Language - Khmer'), (27, b'Unindexed Language - Korean'), (44, b'Unindexed Language - Kyrgyz'), (47, b'Unindexed Language - Kurdish'), (54, b'Unindexed Language - Lao'), (41, b'Unindexed Language - Macedonian'), (55, b'Unindexed Language - Marathi'), (48, b'Unindexed Language - Mongolian'), (52, b'Unindexed Language - Nepali'), (57, b'Unindexed Language - Oriya'), (39, b'Unindexed Language - Punjabi'), (40, b'Unindexed Language - Pashto'), (28, b'Unindexed Language - Russian or Other Cyrillic'), (33, b'Unindexed Language - Serbian'), (36, b'Unindexed Language - Sinhala'), (38, b'Unindexed Language - Tagalog'), (51, b'Unindexed Language - Tamil'), (42, b'Unindexed Language - Telugu'), (30, b'Unindexed Language - Thai'), (53, b'Unindexed Language - Uighur'), (35, b'Unindexed Language - Urdu'), (29, b'Unindexed Language - Vietnamese'), (9, b'Piracy'), (10, b'Human Rights Abuses'), (11, b'Ad Server'), (12, b'URL Shortener'), (13, b'No Content'), (14, b'Malware'), (200, b'Quality Content'), (201, b'Partner Site')]),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_country',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_org',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
