# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_booktickets_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktickets',
            name='price',
            field=models.FloatField(),
        ),
    ]
