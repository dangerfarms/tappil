# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField()),
                ('deep_link', models.TextField()),
                ('referrer', models.ForeignKey(related_name='links', to='referrers.Referrer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
