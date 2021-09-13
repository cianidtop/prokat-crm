from django.db import models



class Client(models.Model):
    DOCUMENT = (
    ('Паспорт', 'Паспорт'),
    ('Водительское удостоверение', 'Водительское удостоверение'),
    )

    phone_number = models.CharField('Номер Телефона', default='', max_length=15)
    document = models.CharField('Вид документа', choices=DOCUMENT, default='Паспорт', max_length=30)
    document_series = models.CharField('Серия документа', default='', max_length=15)
    document_number = models.CharField('Номер документа', default='', max_length=15)
    first_name = models.CharField('Имя:', default='', max_length=20)
    last_name = models.CharField('Фамилия:', default='', max_length=20)
    middle_name = models.CharField('Отчество', default='', max_length=20)
    ready = models.BooleanField('Согласен(-на) с пользовательским соглашением', default=False)
    sign = models.ImageField(default='default.jpg', upload_to='user_images')
    start_time = models.DateTimeField('Время регистрации', auto_now=True)
    bonus = models.IntegerField('Бонусный счет:', default=0)
    comment = models.CharField('Комментарий:', default='-', max_length=255)
