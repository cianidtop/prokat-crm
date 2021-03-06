# Generated by Django 3.0.4 on 2020-03-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=15, verbose_name='Номер Телефона')),
                ('first_name', models.CharField(default='', max_length=20, verbose_name='Имя:')),
                ('last_name', models.CharField(default='', max_length=20, verbose_name='Фамилия:')),
                ('tariff', models.CharField(choices=[('Полчаса', 'Полчаса'), ('Час', 'Час'), ('Поминутный', 'Поминутный')], default='', max_length=20, verbose_name='Тариф')),
            ],
        ),
    ]
