# Generated by Django 2.2.16 on 2022-08-31 23:37

import common.models.base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_notice', '0007_auto_20220831_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskbroadcast',
            name='broadcast_num',
            field=models.IntegerField(default=0, verbose_name='同一节点播报次数'),
        ),
        migrations.AddField(
            model_name='taskbroadcast',
            name='next_broadcast_time',
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name='阶梯播报下一次播报时间'),
        ),
    ]