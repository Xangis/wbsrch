# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=120)),
                ('content', models.TextField(help_text=b'Use HTML. Include opening and closing <p> tags because they will not be in the template')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=80)),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
                ('meta_description', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
