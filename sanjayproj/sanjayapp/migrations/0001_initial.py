# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-06 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('environment', models.CharField(max_length=20)),
                ('serialnumber', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='apps',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanjayapp.Host'),
        ),
    ]