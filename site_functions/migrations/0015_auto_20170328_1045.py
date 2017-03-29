# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0014_article_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='confirmation_code',
            field=models.CharField(default='aiahisguaeh', max_length=16),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]