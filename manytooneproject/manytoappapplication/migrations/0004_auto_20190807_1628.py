# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-07 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manytoappapplication', '0003_auto_20190807_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manytoappapplication.Student'),
        ),
    ]
