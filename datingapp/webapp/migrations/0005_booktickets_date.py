# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-14 03:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190212_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktickets',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 3, 40, 29, 315696, tzinfo=utc)),
            preserve_default=False,
        ),
    ]