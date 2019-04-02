# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=100, default='no_name')),
                ('sex', models.CharField(verbose_name='性别', max_length=50, default='male')),
                ('sid', models.CharField(verbose_name='学号', max_length=100, default='0')),
            ],
        ),
    ]
