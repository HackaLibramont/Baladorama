# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0039_auto_20150321_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='distance_from',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 1, 31, 35, 92598)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 1, 31, 35, 92617)),
            preserve_default=True,
        ),
    ]
