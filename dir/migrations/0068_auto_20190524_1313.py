# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0067_auto_20190519_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'in_db': 'indexes',
            },
        ),
        migrations.AlterField(
            model_name='apisubscription',
            name='user',
            field=models.ForeignKey(to='dir.APIUser'),
        ),
        migrations.AlterField(
            model_name='apiusage',
            name='user',
            field=models.ForeignKey(to='dir.APIUser'),
        ),
    ]
