# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_collections', '0002_collection_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='itemCustomFields',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
