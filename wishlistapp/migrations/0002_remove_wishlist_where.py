# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='where',
        ),
    ]
