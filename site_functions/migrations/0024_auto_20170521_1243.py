# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0023_userprofile_have_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicurso',
            name='begin',
            field=models.CharField(max_length=1024),
        ),
    ]
