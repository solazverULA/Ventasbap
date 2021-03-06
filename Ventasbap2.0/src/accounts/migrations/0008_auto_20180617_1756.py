# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-18 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180617_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bday',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ci',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
