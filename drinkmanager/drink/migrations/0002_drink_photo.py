# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='photo',
            field=models.ImageField(default='uploads/canette_coca.jpeg', upload_to='uploads/'),
        ),
    ]
