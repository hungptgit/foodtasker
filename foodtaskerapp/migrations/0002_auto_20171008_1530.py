# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurent',
            new_name='Restaurant',
        ),
    ]
