# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160209_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
