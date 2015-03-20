# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0008_auto_20150320_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='phone',
            field=models.CharField(max_length=45, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 22, 7, 16, 151507)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 22, 7, 16, 151532)),
            preserve_default=True,
        ),
    ]
