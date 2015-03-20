# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0005_auto_20150320_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPX',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('metadata', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPXSegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPXTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('gpx', models.ForeignKey(to='baladapp.GPX')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPXWaypoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('segment', models.ForeignKey(to='baladapp.GPXSegment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gpxsegment',
            name='track',
            field=models.ForeignKey(to='baladapp.GPXTrack'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 22, 4, 3, 644270)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 22, 4, 3, 644296)),
            preserve_default=True,
        ),
    ]
