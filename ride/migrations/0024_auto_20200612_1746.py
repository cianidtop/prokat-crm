# Generated by Django 3.0.7 on 2020-06-12 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0023_auto_20200605_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 18, 16, 37, 830663), verbose_name='Время окончания поездки'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='tech',
            field=models.CharField(choices=[('Самокат', 'Самокат'), ('Байк', 'Байк'), ('Велосипед', 'Велосипед'), ('Машинка', 'Машинка')], default='', max_length=20, verbose_name='Техника:'),
        ),
    ]
