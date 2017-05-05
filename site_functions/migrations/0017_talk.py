# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0016_auto_20170329_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk_name', models.CharField(max_length=256)),
                ('talk_speaker', models.CharField(max_length=256)),
                ('talk_description', models.CharField(max_length=4096)),
                ('talk_begin', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]