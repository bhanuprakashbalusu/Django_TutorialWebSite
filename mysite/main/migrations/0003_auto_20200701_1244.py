# Generated by Django 3.0.7 on 2020-07-01 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200630_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 12, 44, 48, 273755), verbose_name='date published'),
        ),
    ]
