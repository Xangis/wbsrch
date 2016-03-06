# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0007_urlparameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlparameter',
            name='only_replace_if_present',
            field=models.BooleanField(default=False, help_text=b'Only replace the URL parameter if it is already present.'),
            preserve_default=True,
        ),
    ]
