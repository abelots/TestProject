# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_attached_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
