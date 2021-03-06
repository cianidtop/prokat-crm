# Generated by Django 3.0.4 on 2020-03-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_auto_20200312_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='summ',
            field=models.CharField(default='', max_length=20, verbose_name='Стоимость:'),
        ),
        migrations.AddField(
            model_name='ride',
            name='tech_quantity',
            field=models.CharField(choices=[('Самокат', 'Самокат'), ('Байк', 'Байк'), ('Велосипед', 'Велосипед')], default='', max_length=20, verbose_name='Количество Техники:'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='tech_number',
            field=models.CharField(default='', max_length=20, verbose_name='Номер техники:'),
        ),
    ]
