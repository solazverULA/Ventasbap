# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-10 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ci',
            field=models.IntegerField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
