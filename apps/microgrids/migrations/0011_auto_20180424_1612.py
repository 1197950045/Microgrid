# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microgrids', '0010_auto_20180424_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webmicrogrid',
            name='area_type',
            field=models.IntegerField(choices=[(0, '间隔区'), (1, '光伏区'), (2, '风力区'), (3, '燃机区'), (4, '电池储能区'), (5, '飞轮储能区'), (6, '控制区'), (7, '环境')], verbose_name='区域类别'),
        ),
        migrations.AlterField(
            model_name='webmicrogrid',
            name='parent_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='microgrids.WebMicrogrid', to_field='num', verbose_name='设备所属区'),
        ),
    ]
