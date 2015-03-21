# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0041_auto_20150321_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpxsegment',
            name='track',
        ),
        migrations.RemoveField(
            model_name='gpxtrack',
            name='gpx',
        ),
        migrations.DeleteModel(
            name='GPX',
        ),
        migrations.DeleteModel(
            name='GPXTrack',
        ),
        migrations.RemoveField(
            model_name='gpxwaypoint',
            name='segment',
        ),
        migrations.DeleteModel(
            name='GPXSegment',
        ),
        migrations.DeleteModel(
            name='GPXWaypoint',
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 46, 52, 51035)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 46, 52, 51077)),
            preserve_default=True,
        ),
    ]
