# Generated by Django 3.1.7 on 2021-06-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20200530_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='comment',
            field=models.CharField(default='', max_length=255, verbose_name='Комментарий:'),
        ),
    ]
