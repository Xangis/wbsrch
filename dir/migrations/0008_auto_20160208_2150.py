# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0007_auto_20160116_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoComplete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_af',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_bm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_br',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_cs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_cy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_da',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_de',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_el',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_eo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_es',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_et',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_eu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_fi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_fo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_fr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_fy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_gl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_hr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_hu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_is',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_it',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_kg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_la',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_lg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ln',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_lt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_lv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_nap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_nl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_no',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_nso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ny',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_oc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_om',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_pl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_pms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_pt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_rn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_rw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_scn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_so',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_st',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_sw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_tn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_tr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_ve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_vec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_wo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_xh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_yo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.CreateModel(
            name='AutoComplete_zu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-score'],
                'abstract': False,
                'in_db': 'indexes',
            },
        ),
        migrations.AlterField(
            model_name='indexterm',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_af',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ak',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_bm',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_br',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_da',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ee',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ff',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fy',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ig',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_is',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_kg',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ki',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_la',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lg',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ln',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nap',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_no',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nso',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ny',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_oc',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_om',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pms',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rn',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sc',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_scn',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sk',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ss',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_st',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tn',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ts',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ve',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_vec',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results found in the database (max 1000000), or for mutli-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
    ]
