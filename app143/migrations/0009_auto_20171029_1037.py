# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-29 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app143', '0008_auto_20170918_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='multiauthoebooks',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='multiplebooks',
            old_name='author',
            new_name='user',
        ),
    ]
