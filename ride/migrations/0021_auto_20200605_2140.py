# Generated by Django 2.2.7 on 2020-06-05 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0020_auto_20200530_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 5, 22, 10, 48, 260984), verbose_name='Время окончания поездки'),
        ),
    ]