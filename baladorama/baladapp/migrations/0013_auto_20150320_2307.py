# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0012_auto_20150320_2246'),
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
            model_name='poi',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poi',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 23, 7, 15, 490962)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='start_latitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='start_longitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='stop_latitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='stop_longitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 23, 7, 15, 490985)),
            preserve_default=True,
        ),
    ]
