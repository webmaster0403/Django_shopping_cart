# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_auto_20171211_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='billing_method',
            new_name='payment_method',
        ),
    ]
