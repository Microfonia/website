# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microfonia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('episode_number', models.IntegerField()),
                ('episode_name', models.CharField(max_length=50)),
                ('episode_date', models.DateField()),
                ('episode_sinopsis', models.TextField()),
                ('episode_cast', models.TextField()),
                ('episode_url', models.URLField()),
            ],
        ),
    ]
