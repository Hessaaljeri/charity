# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170414_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('date_time', models.DateTimeField()),
                ('reason', models.TextField(default=b'')),
                ('email', models.EmailField(max_length=254)),
                ('twitter_id', models.CharField(default=b'', max_length=50, blank=True)),
                ('phone', models.CharField(default=b'', max_length=20, blank=True)),
                ('approved', models.NullBooleanField()),
                ('sent_1st_reminder', models.BooleanField(default=False)),
                ('sent_2nd_reminder', models.BooleanField(default=False)),
                ('charity', models.ForeignKey(to='app.Charity')),
            ],
        ),
    ]
