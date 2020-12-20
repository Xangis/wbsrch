# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0065_auto_20190512_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domainsuffix',
            options={'ordering': ['extension']},
        ),
    ]
