# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParraINC', '0002_auto_20160325_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='control_calidad',
            field=models.BooleanField(default=False),
        ),
    ]
