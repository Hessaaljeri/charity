# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('Phone', models.CharField(max_length=8, null=True, blank=True)),
                ('Fax', models.CharField(max_length=8, null=True, blank=True)),
                ('Logo', models.ImageField(upload_to=b'')),
                ('Location', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
