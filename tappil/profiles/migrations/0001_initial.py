# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField()),
                ('device_family', models.TextField()),
                ('device_os', models.TextField()),
                ('device_version', models.TextField()),
                ('uuid', models.TextField()),
                ('meta_data', jsonfield.fields.JSONField()),
                ('link', models.ForeignKey(related_name='profiles', to='links.Link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
