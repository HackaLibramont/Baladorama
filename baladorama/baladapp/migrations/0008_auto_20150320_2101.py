# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0007_auto_20150320_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 21, 1, 51, 604306)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 21, 1, 51, 604326)),
            preserve_default=True,
        ),
    ]
