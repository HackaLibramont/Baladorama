# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0034_auto_20150321_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.DecimalField(max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.DecimalField(max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 0, 12, 51, 83950)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 0, 12, 51, 83977)),
            preserve_default=True,
        ),
    ]
