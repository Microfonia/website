# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microfonia', '0003_serie_abbrev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='img',
            field=models.ImageField(upload_to='episodes/'),
        ),
    ]