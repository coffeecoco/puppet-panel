# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
