# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20171120_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postpic',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(blank=True, default=b'default_profile_picture.png', upload_to=b'', verbose_name='profoto'),
        ),
    ]
