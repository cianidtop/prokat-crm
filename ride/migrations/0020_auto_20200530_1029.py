# Generated by Django 2.2.7 on 2020-05-30 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0019_auto_20200530_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 10, 59, 18, 199058), verbose_name='Время окончания поездки'),
        ),
    ]
