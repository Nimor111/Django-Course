# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-04 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20170404_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]