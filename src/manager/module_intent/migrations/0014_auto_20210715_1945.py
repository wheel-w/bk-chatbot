# Generated by Django 2.2.6 on 2021-07-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_intent', '0013_auto_20210715_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='executionlog',
            name='feature_id',
            field=models.CharField(default='', max_length=128, verbose_name='流水线ID'),
        ),
        migrations.AddField(
            model_name='executionlog',
            name='project_id',
            field=models.CharField(default='', max_length=128, verbose_name='项目ID'),
        ),
    ]
