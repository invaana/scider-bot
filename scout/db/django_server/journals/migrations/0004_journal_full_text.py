# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_auto_20170111_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='full_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]