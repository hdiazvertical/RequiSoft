# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0006_auto_20161006_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
