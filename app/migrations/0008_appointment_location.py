# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170512_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Location',
            field=geoposition.fields.GeopositionField(default=1, max_length=42),
            preserve_default=False,
        ),
    ]
