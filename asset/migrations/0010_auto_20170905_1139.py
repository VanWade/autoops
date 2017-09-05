# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0009_auto_20170904_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='hostname',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='model',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='型号'),
        ),
    ]
