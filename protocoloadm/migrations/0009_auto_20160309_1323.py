# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-09 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocoloadm', '0008_auto_20160308_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='numero',
            field=models.PositiveIntegerField(verbose_name='Número de Protocolo'),
        ),
    ]