# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GeoPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('author', models.CharField(max_length=200)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='geopoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.GeoPoint'),
        ),
    ]
