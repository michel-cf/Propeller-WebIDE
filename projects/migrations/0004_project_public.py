# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-07 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]