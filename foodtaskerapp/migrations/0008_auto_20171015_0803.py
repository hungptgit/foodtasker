# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0007_auto_20171015_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='totals',
            new_name='total',
        ),
    ]
