# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0013_auto_20170317_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]