# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0025_auto_20150715_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 15, 14, 55, 6, 661099, tzinfo=utc)),
        ),
    ]