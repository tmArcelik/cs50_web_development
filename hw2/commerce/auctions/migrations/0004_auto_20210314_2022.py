# Generated by Django 3.1.4 on 2021-03-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210314_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='imagePath',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
