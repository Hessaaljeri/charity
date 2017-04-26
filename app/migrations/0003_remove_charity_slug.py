# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_charity_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charity',
            name='slug',
        ),
    ]
