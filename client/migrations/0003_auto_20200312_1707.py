# Generated by Django 3.0.4 on 2020-03-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20200312_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sign',
            field=models.ImageField(default='default.jpg', upload_to='user_images'),
        ),
        migrations.AlterField(
            model_name='client',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='Согласен(-на) с пользовательским соглашением'),
        ),
    ]
