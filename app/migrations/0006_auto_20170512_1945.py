# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='sent_1st_reminder',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='sent_2nd_reminder',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='twitter_id',
        ),
    ]
