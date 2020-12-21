# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0034_autocomplete_et_autocomplete_hr_autocomplete_lt_autocomplete_lv_indexterm_et_indexterm_hr_indexterm_'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResultClick_ee',
        ),
        migrations.DeleteModel(
            name='SearchLog_ee',
        ),
    ]
