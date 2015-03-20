# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0006_auto_20150320_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_start', models.BooleanField(default=False)),
                ('is_stop', models.BooleanField(default=False)),
                ('city', models.ForeignKey(to='baladapp.City')),
                ('walk', models.ForeignKey(to='baladapp.Walk')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='walk',
            name='cities',
            field=models.ManyToManyField(to='baladapp.City', through='baladapp.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='pois',
            field=models.ManyToManyField(to='baladapp.Poi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 21, 0, 58, 843337)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 21, 0, 58, 843357)),
            preserve_default=True,
        ),
    ]
