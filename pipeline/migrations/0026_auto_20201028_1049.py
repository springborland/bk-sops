# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-28 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pipeline", "0025_auto_20200813_1216"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pipelinetemplate",
            name="name",
            field=models.CharField(db_index=True, default="default_template", max_length=128, verbose_name="模板名称"),
        ),
    ]
