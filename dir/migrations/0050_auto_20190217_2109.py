# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0049_auto_20190217_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='domain',
            field=models.OneToOneField(to='dir.DomainInfo'),
        ),
    ]
