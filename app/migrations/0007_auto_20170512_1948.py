# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170512_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='reason',
            new_name='note',
        ),
    ]
