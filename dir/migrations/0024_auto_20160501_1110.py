# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0023_ipsearchlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultclick',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_af',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ak',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_bm',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_br',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ca',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_cs',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_cy',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_da',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_de',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ee',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_el',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_eo',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_es',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_et',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_eu',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ff',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_fi',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_fo',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_fr',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_fy',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_gl',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ha',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_hr',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_hu',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ig',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_is',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_it',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_kg',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ki',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_la',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_lg',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ln',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_lt',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_lv',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_nap',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_nl',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_no',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_nso',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ny',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_oc',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_om',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_pl',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_pms',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_pt',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_rn',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ro',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_rw',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sc',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_scn',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sk',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sl',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sn',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_so',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ss',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_st',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sv',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_sw',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_tn',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_tr',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ts',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_ve',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_vec',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_wo',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_xh',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_yo',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='resultclick_zu',
            name='search_id',
        ),
        migrations.AddField(
            model_name='domainsearchlog',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='ipsearchlog',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_af',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ak',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_bm',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_br',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ca',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_cs',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_cy',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_da',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_de',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ee',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_el',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_eo',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_es',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_et',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_eu',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ff',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_fi',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_fo',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_fr',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_fy',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_gl',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ha',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_hr',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_hu',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ig',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_is',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_it',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_kg',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ki',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_la',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_lg',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ln',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_lt',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_lv',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_nap',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_nl',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_no',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_nso',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ny',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_oc',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_om',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_pl',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_pms',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_pt',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_rn',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ro',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_rw',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sc',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_scn',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sk',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sl',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sn',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_so',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ss',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_st',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sv',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_sw',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_tn',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_tr',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ts',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_ve',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_vec',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_wo',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_xh',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_yo',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='searchlog_zu',
            name='search_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, db_index=True),
        ),
    ]
