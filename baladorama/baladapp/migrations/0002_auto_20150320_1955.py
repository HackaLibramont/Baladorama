# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='start_latitude',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='start_longitude',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='stop_latitude',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='stop_longitude',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walk',
            name='name',
            field=models.CharField(max_length=45, null=True),
            preserve_default=True,
        ),
    ]
