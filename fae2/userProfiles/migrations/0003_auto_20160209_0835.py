# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfiles', '0002_auto_20160208_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ws_report_group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='websiteResultGroups.WebsiteReportGroup'),
        ),
    ]
