# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0055_auto_20150321_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='city',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 38, 32, 106879)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 38, 32, 106899)),
            preserve_default=True,
        ),
    ]
