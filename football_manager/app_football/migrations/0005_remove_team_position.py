# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_football', '0004_auto_20170404_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='position',
        ),
    ]
