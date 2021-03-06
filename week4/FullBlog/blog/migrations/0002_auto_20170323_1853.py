# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 18:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='authors',
            field=models.ManyToManyField(related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
