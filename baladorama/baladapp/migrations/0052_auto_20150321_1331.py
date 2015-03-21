# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0051_auto_20150321_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='parent_poi_type',
            field=models.ForeignKey(related_name='parent_poi', to='baladapp.PoiType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='q_culture',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='q_food',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='q_heritage',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='q_nature',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poi',
            name='poi_type',
            field=models.ForeignKey(related_name='child_poi', to='baladapp.PoiType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 13, 31, 0, 927739)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 13, 31, 0, 927756)),
            preserve_default=True,
        ),
    ]
