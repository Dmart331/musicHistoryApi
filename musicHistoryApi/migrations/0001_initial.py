# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Album')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Album')),
                ('artist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Genre')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='song_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Song'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='song_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicHistoryApi.Song'),
        ),
    ]
