# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-20 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desarrolladores', '0002_auto_20190120_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='desarrollador',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]