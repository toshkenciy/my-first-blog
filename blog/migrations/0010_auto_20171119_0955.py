# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 02:55
from __future__ import unicode_literals

from cloudinary.models import CloudinaryField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_profile_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profpic',

            field =  CloudinaryField('image')
        ),
    ]
