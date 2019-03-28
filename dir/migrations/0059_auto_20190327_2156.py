# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0058_auto_20190319_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexterm',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_an',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_ca',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_cs',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_cy',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_de',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_el',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_es',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_et',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_eu',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_fi',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_fr',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_gl',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_ha',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_hr',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_hu',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_it',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_lt',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_lv',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_nl',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_pl',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_pt',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_ro',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_rw',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_sl',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_sn',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_so',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_sv',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_sw',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_tr',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_wo',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_xh',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_yo',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indexterm_zu',
            name='num_pages',
            field=models.IntegerField(help_text=b'The number of pages found in the database for this term (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_an',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='num_results',
            field=models.IntegerField(help_text=b'The number of results shown in search (max 200), or for multi-word, the number of exact matches found in the database.', null=True, blank=True),
        ),
    ]
