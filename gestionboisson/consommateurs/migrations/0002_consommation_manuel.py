# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consommateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consommation',
            name='manuel',
            field=models.BooleanField(default=True),
        ),
    ]