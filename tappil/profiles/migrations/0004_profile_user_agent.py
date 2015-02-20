# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150220_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_agent',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
