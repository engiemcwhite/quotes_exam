# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20180323_1129'),
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='favoritedby',
        ),
        migrations.AddField(
            model_name='list',
            name='quotes',
            field=models.ManyToManyField(related_name='lists', to='quotes.Quote'),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='registration.User'),
        ),
    ]
