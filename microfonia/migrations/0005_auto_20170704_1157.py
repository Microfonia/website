# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microfonia', '0004_auto_20170704_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='img',
            field=models.ImageField(upload_to='series/'),
        ),
    ]
