# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-07 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20181008_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturevideo',
            name='slug',
        ),
    ]
