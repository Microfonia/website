# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=2)),
                ('download', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('cast', models.TextField()),
                ('sinopsis', models.TextField()),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microfonia.Serie'),
        ),
    ]
