# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170323_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
