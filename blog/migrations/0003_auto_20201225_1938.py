# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-26 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150925_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(help_text='Use HTML. Include opening and closing <p> tags because they will not be in the template'),
        ),
    ]
