# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 00:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL),
        ),
    ]
