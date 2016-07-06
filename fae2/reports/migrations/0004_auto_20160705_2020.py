# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20160701_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitereport',
            name='max_pages',
            field=models.IntegerField(choices=[(5, b'   5 pages'), (10, b'  10 pages'), (25, b'  25 pages'), (50, b'  50 pages'), (100, b' 100 pages'), (200, b' 200 pages'), (400, b' 400 pages'), (800, b' 800 pages'), (1600, b'1600 pages')], default=0, verbose_name=b'Maximum Pages'),
        ),
    ]
