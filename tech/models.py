from django.db import models

# Create your models here.
class Tech(models.Model):
    TECH = (
        ('Самокат', 'Самокат'),
        ('Байк', 'Байк'),
        ('Велосипед', 'Велосипед')
    )

    tech = models.CharField('Техника:', default='', choices=TECH, max_length=20)
    tech_number = models.CharField('Номер техники:', default='', max_length=20)
    reason = models.TextField('Вид поломки', default='', max_length=150)
    start_time = models.DateTimeField('Время поломки', auto_now=True)


