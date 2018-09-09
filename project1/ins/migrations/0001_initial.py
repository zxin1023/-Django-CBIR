# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-08 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='img')),
                ('img_name', models.TextField(default='pics')),
                ('img_tags', models.TextField(default='tags')),
                ('img_uploader', models.TextField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10, unique=True)),
                ('user_pass', models.CharField(max_length=10)),
            ],
        ),
    ]
