# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ruleCategories', '0001_initial'),
        ('reports', '0009_auto_20160204_2200'),
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteGuidelineResultGroup',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(default=b'none', editable=False, max_length=16)),
                ('rule_scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.RuleScope')),
            ],
            options={
                'ordering': ['-rule_scope'],
                'verbose_name': 'Website Rule Scope Result Group',
                'verbose_name_plural': 'Website Rule Scope Result Groups',
            },
        ),
        migrations.CreateModel(
            name='WebsiteReportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('num_total_pages', models.IntegerField(default=0)),
                ('num_total_reports', models.IntegerField(default=0)),
                ('ws_reports', models.ManyToManyField(blank=True, to='reports.WebsiteReport')),
            ],
            options={
                'verbose_name': 'Website Report Group',
                'verbose_name_plural': 'Website Report Groups',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRuleCategoryResultGroup',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(default=b'none', editable=False, max_length=16)),
                ('rule_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruleCategories.RuleCategory')),
                ('wsr_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rc_result_groups', to='websiteResultGroups.WebsiteReportGroup')),
            ],
            options={
                'ordering': ['rule_category'],
                'verbose_name': 'Website Rule Category Result Group',
                'verbose_name_plural': 'Website Rule Category Result Groups',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRuleResultGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'C', b'Complete')], default=b'U', max_length=2, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('slug', models.SlugField(default=b'none', editable=False, max_length=16)),
                ('pages_violation', models.IntegerField(default=0)),
                ('pages_warning', models.IntegerField(default=0)),
                ('pages_manual_check', models.IntegerField(default=0)),
                ('pages_passed', models.IntegerField(default=0)),
                ('pages_na', models.IntegerField(default=0)),
                ('pages_with_hidden_content', models.IntegerField(default=0)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Rule')),
                ('wsr_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rule_result_groups', to='websiteResultGroups.WebsiteReportGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='websiteguidelineresultgroup',
            name='wsr_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rs_result_groups', to='websiteResultGroups.WebsiteReportGroup'),
        ),
    ]
