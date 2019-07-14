from django.db import models
from entity.models import Entity


class Contarcts(models.Model):
    """Модель контракта"""

    number_contr = models.CharField('Номер контракта', primary_key=True, max_length=20)
    customer = models.ForeignKey('Customers', verbose_name='Заказчик', on_delete=models.CASCADE, blank=True)
    txt_contacts = models.TextField('Условия контракта', null=True, blank=True)
    date_pub = models.DateField('Дата публикации', blank=True)
    date_rec = models.DateField('Дата приёма', blank=True)
    offer = models.ManyToManyField(Entity, verbose_name='Контрагенты', related_name='contarcts_entity')
    sum_contr = models.PositiveIntegerField('Сумма контракта', blank=True)
    close = models.BooleanField('Закрыт', blank=True)
    cancel_contr = models.BooleanField('Отменён', blank=True)
    deadline = models.BooleanField('Превышение сроков', blank=True)
    fine = models.PositiveIntegerField('Штрафные суммы', null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class Customers(models.Model):
    inn = models.TextField('ИНН заказчика', primary_key=True, blank=True)
    ogrn = models.CharField('ОГРН заказчика', max_length=20, blank=True)
    name_customer = models.CharField('Наименование организации', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

# Create your models here.
