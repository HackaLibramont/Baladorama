# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0003_auto_20150320_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='avg_bike_duration',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='avg_horse_duration',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='avg_walker_duration',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 20, 16, 1, 164128)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='is_for_bike',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='is_for_disabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='is_for_horse',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='is_loop',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 20, 16, 1, 164151)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='waypoints',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
