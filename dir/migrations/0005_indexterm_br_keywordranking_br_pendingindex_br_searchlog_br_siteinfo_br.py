# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0004_auto_20151222_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexTerm_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(unique=True, max_length=240)),
                ('date_indexed', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_rankings', models.TextField()),
                ('num_results', models.IntegerField(null=True, blank=True)),
                ('index_time', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('search_results', models.TextField(null=True, blank=True)),
                ('actively_blocked', models.BooleanField(default=False)),
                ('refused', models.BooleanField(default=False)),
                ('typo_for', models.CharField(help_text=b'A phrase that this search term is a possible typo for.', max_length=240, null=True, blank=True)),
                ('is_language', models.CharField(help_text=b'This is a word in language X, and will show a link to that index in search results.', max_length=4, null=True, blank=True)),
                ('term_weight', models.IntegerField(help_text=b'Term weight in percent. Used for multi-word terms. If set below 100, this term will count less than other words.', null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeywordRanking_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(max_length=240, db_index=True)),
                ('rank', models.IntegerField()),
                ('rooturl', models.CharField(db_index=True, max_length=260, blank=True)),
                ('show', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PendingIndex_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(unique=True, max_length=240)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('reason', models.CharField(max_length=240, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchLog_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('result_count', models.IntegerField()),
                ('last_search', models.DateTimeField(auto_now_add=True)),
                ('search_time', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('indexed', models.BooleanField(default=False)),
                ('referer', models.CharField(max_length=255, null=True, blank=True)),
                ('ip', models.CharField(max_length=16, null=True, blank=True)),
                ('browserstring', models.CharField(max_length=255, null=True, blank=True)),
                ('is_bot', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'in_db': 'indexes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteInfo_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rooturl', models.CharField(max_length=260, blank=True)),
                ('url', models.CharField(unique=True, max_length=2048, blank=True)),
                ('pagetitle', models.CharField(max_length=260, null=True, blank=True)),
                ('pagedescription', models.CharField(max_length=320, null=True, blank=True)),
                ('pagefirstheadtag', models.CharField(max_length=260, null=True, blank=True)),
                ('pagefirsth2tag', models.CharField(max_length=260, null=True, blank=True)),
                ('pagefirsth3tag', models.CharField(max_length=260, null=True, blank=True)),
                ('pagekeywords', models.CharField(max_length=260, null=True, blank=True)),
                ('pagecontents', models.TextField(null=True, blank=True)),
                ('pagetext', models.TextField(null=True, blank=True)),
                ('pagesize', models.IntegerField(null=True, blank=True)),
                ('lastcrawled', models.DateTimeField(null=True, blank=True)),
                ('firstcrawled', models.DateTimeField(null=True, blank=True)),
                ('ip', models.CharField(db_index=True, max_length=16, null=True, blank=True)),
                ('num_errors', models.IntegerField(default=0, blank=True)),
                ('error_info', models.TextField(default=b'', blank=True)),
                ('server_header', models.CharField(max_length=128, null=True, blank=True)),
                ('content_type_header', models.CharField(max_length=100, null=True, blank=True)),
                ('num_css_files', models.IntegerField(help_text=b'Number of external CSS files.', null=True, blank=True)),
                ('num_images', models.IntegerField(null=True, blank=True)),
                ('num_javascripts', models.IntegerField(help_text=b'Number of external JavaScript files.', null=True, blank=True)),
                ('num_iframes', models.IntegerField(null=True, blank=True)),
                ('num_audio_tags', models.IntegerField(null=True, blank=True)),
                ('num_video_tags', models.IntegerField(null=True, blank=True)),
                ('num_svg_tags', models.IntegerField(null=True, blank=True)),
                ('num_canvas_tags', models.IntegerField(null=True, blank=True)),
                ('image_alt_tags', models.TextField(null=True, blank=True)),
                ('image_title_tags', models.TextField(null=True, blank=True)),
                ('image_filenames', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
