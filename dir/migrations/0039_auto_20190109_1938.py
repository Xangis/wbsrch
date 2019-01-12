# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0038_autocomplete_ca_autocomplete_sl_indexterm_ca_indexterm_sl_keywordranking_ca_keywordranking_sl_pendin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='whois_state',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
