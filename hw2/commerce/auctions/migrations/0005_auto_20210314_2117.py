# Generated by Django 3.1.4 on 2021-03-14 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210314_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='endTime',
            field=models.TimeField(default=datetime.datetime(2021, 3, 14, 21, 17, 35, 373771)),
        ),
        migrations.AddField(
            model_name='auction',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2021, 3, 14, 21, 17, 35, 373771)),
        ),
    ]
