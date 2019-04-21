# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0059_auto_20190327_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexterm',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_an',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_an',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_an',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_an',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ca',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cs',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_cy',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_de',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_el',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_es',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_et',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_eu',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fi',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_fr',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_gl',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ha',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hr',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_hu',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_it',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lt',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_lv',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_nl',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pl',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_pt',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_ro',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_rw',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sl',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sn',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_so',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sv',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_sw',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_tr',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_wo',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_xh',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_yo',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='index_time',
            field=models.DecimalField(help_text=b'in seconds', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='num_pages',
            field=models.IntegerField(help_text=b'Number of pages found in the database (max 1000000).', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='num_results',
            field=models.IntegerField(help_text=b'Number of results shown in search (max 200), or for multi-word, number of exact matches found in the db.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexterm_zu',
            name='term_weight',
            field=models.IntegerField(help_text=b'Term weight in percent (for multi-word terms). If set below 100, this term will count less than other words.', null=True, blank=True),
        ),
    ]
