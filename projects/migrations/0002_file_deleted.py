# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-07 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]