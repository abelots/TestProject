# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20161009_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincomment',
            name='file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]