# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0048_auto_20190214_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_taken', models.DateField(auto_now_add=True)),
                ('icon', models.ImageField(upload_to=b'favicons')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='favicons_last_updated',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='domain',
            field=models.ForeignKey(to='dir.DomainInfo', unique=True),
        ),
        migrations.AddField(
            model_name='favicon',
            name='domain',
            field=models.ForeignKey(to='dir.DomainInfo'),
        ),
    ]
