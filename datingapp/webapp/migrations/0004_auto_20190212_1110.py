# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190212_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktickets',
            name='price',
        ),
        migrations.AlterField(
            model_name='booktickets',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]