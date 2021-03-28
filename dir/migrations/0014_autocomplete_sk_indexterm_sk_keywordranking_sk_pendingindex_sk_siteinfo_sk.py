# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-28 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0013_auto_20210325_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoComplete_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(db_index=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexTerm_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=240, unique=True)),
                ('date_indexed', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_rankings', models.TextField()),
                ('num_results', models.IntegerField(blank=True, help_text='Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True)),
                ('num_pages', models.IntegerField(blank=True, help_text='Number of pages found in the database (max 1000000).', null=True)),
                ('index_time', models.DecimalField(blank=True, decimal_places=2, help_text='in seconds', max_digits=8, null=True)),
                ('search_results', models.TextField(blank=True, null=True)),
                ('actively_blocked', models.BooleanField(default=False)),
                ('refused', models.BooleanField(default=False)),
                ('typo_for', models.CharField(blank=True, help_text='A phrase that this search term is a possible typo for.', max_length=240, null=True)),
                ('is_language', models.CharField(blank=True, help_text='This is a word in language X, and will show a link to that index in search results.', max_length=4, null=True)),
                ('term_weight', models.IntegerField(blank=True, help_text='Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordRanking_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(db_index=True, max_length=240)),
                ('rank', models.IntegerField()),
                ('rooturl', models.CharField(blank=True, db_index=True, max_length=260)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PendingIndex_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=240, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(blank=True, max_length=240, null=True)),
                ('priority', models.IntegerField(blank=True, choices=[(0, 'Highest'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Lowest')], db_index=True, default=2)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo_sk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooturl', models.CharField(blank=True, max_length=260)),
                ('url', models.CharField(blank=True, max_length=2048, unique=True)),
                ('pagetitle', models.CharField(blank=True, max_length=260, null=True)),
                ('pagedescription', models.CharField(blank=True, max_length=320, null=True)),
                ('pagefirstheadtag', models.CharField(blank=True, max_length=260, null=True)),
                ('pagefirsth2tag', models.CharField(blank=True, max_length=260, null=True)),
                ('pagefirsth3tag', models.CharField(blank=True, max_length=260, null=True)),
                ('pagekeywords', models.CharField(blank=True, max_length=260, null=True)),
                ('pagetext', models.TextField(blank=True, null=True)),
                ('pagesize', models.IntegerField(blank=True, null=True)),
                ('lastcrawled', models.DateTimeField(blank=True, null=True)),
                ('firstcrawled', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, db_index=True, max_length=16, null=True)),
                ('num_errors', models.IntegerField(blank=True, default=0)),
                ('error_info', models.TextField(blank=True, default='')),
                ('server_header', models.CharField(blank=True, max_length=128, null=True)),
                ('content_type_header', models.CharField(blank=True, max_length=100, null=True)),
                ('num_css_files', models.IntegerField(blank=True, help_text='Number of external CSS files.', null=True)),
                ('num_images', models.IntegerField(blank=True, null=True)),
                ('num_javascripts', models.IntegerField(blank=True, help_text='Number of external JavaScript files.', null=True)),
                ('num_iframes', models.IntegerField(blank=True, null=True)),
                ('num_audio_tags', models.IntegerField(blank=True, null=True)),
                ('num_video_tags', models.IntegerField(blank=True, null=True)),
                ('num_svg_tags', models.IntegerField(blank=True, null=True)),
                ('num_canvas_tags', models.IntegerField(blank=True, null=True)),
                ('image_alt_tags', models.TextField(blank=True, null=True)),
                ('image_title_tags', models.TextField(blank=True, null=True)),
                ('image_filenames', models.TextField(blank=True, null=True)),
                ('simhash_value', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
            ],
        ),
    ]
