# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0011_auto_20160315_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='domain_updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
