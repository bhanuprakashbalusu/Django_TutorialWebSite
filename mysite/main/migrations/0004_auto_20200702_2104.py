# Generated by Django 3.0.7 on 2020-07-02 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200701_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 21, 4, 15, 190720), verbose_name='date published'),
        ),
    ]
