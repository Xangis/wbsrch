# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0066_auto_20190512_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='blocked_to_crawled_ratio',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='domcop_pagerank',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='domcop_pagerank_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='domcop_pagerank_outdated',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='domcop_rank',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='majestic_refsubnets',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='quantcast_outdated',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='quantcast_rank',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='quantcast_rank_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
