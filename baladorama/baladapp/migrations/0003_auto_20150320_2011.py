# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baladapp', '0002_auto_20150320_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='distance',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walk',
            name='is_for_walker',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
