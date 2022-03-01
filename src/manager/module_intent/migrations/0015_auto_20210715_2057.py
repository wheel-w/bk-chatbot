# Generated by Django 2.2.6 on 2021-07-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_intent', '0014_auto_20210715_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executionlog',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='executionlog',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='executionlog',
            name='feature_id',
            field=models.CharField(default='', max_length=128, verbose_name='特色ID:蓝盾-流水线ID'),
        ),
    ]
