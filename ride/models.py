from django.db import models
from django.contrib.auth.models import User
from datetime import *

class Ride(models.Model):
    end = datetime.now() + timedelta(minutes=30)

    TARIFF = (
    ('Полчаса', 'Полчаса'),
    ('Час', 'Час'),
    ('Поминутный', 'Поминутный')
    )

    TECH = (
        ('Самокат', 'Самокат'),
        ('Байк', 'Байк'),
        ('Велосипед', 'Велосипед'),
        ('Машинка','Машинка')
    )

    PLACES = (
        ('Искра', 'Искра'),
        ('Набережная', 'Набережная')
          )

    TYPES = (
        ('Наличный', 'Наличный'),
        ('Безналичный', 'Безналичный'),
        ('Смешанный', 'Смешанный')
    )

    phone_number = models.CharField('Номер Телефона', default='', max_length=15)
    first_name = models.CharField('Имя:', default='', max_length=20)
    last_name = models.CharField('Фамилия:', default='', max_length=20)
    tech = models.CharField('Техника:', default='', choices=TECH, max_length=20)
    tech_quantity = models.CharField('Количество Техники:', default='', max_length=20)
    tech_number = models.CharField('Номер техники:', default='', max_length=20)
    tariff = models.CharField('Тариф:', default='', choices=TARIFF, max_length=20)
    start_time = models.DateTimeField('Время начала поездки', auto_now_add=True)
    end_time = models.DateTimeField('Время окончания поездки', default=end, auto_now_add=False)
    cena = models.IntegerField('Цена', default=1)
    payment_type = models.CharField('Метод оплаты:', default='', choices=TYPES, max_length=20)
    place_from = models.CharField('Точка выдачи:', default='', choices=PLACES, max_length=20)
    place_to = models.CharField('Точка сдачи:', default='', choices=PLACES, max_length=20)
    ended = models.BooleanField('Поездка окончена', default=False)
