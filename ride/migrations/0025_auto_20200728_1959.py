# Generated by Django 3.0.7 on 2020-07-28 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0024_auto_20200612_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='ended',
            field=models.BooleanField(default=False, verbose_name='Поездка окончена'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 20, 29, 27, 600503), verbose_name='Время окончания поездки'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='first_name',
            field=models.CharField(default='123', max_length=20, verbose_name='Имя:'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='last_name',
            field=models.CharField(default='123', max_length=20, verbose_name='Фамилия:'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='phone_number',
            field=models.CharField(default='123', max_length=15, verbose_name='Номер Телефона'),
        ),
    ]