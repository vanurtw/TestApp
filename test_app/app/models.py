from django.db import models


# Create your models here.


class Customer(models.Model):
    '''Модель Customer'''

    customer_code = models.CharField(
        verbose_name='Код контрагента',
        max_length=255,
    )
    customer_name = models.CharField(
        verbose_name='Наименование',
        max_length=255
    )
    customer_inn = models.CharField(
        verbose_name='ИНН',
        max_length=255
    )
    customer_kpp = models.CharField(
        verbose_name='КПП',
        max_length=255
    )
    customer_legal_address = models.CharField(
        verbose_name='Юр. адрес',
        max_length=255
    )
    customer_postal_address = models.CharField(
        verbose_name='Почтовый адрес',
        max_length=255
    )
    customer_email = models.EmailField(verbose_name='Электронная почта')
    customer_code_main = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name='Вышестоящий контрагент',
        blank=True,
        null=True
    )
    is_organization = models.BooleanField(verbose_name='Юр. лицо')
    is_person = models.BooleanField(verbose_name='Физ. лицо')

    def __str__(self):
        return f'Контрагент {self.customer_name}'

    class Meta:
        verbose_name = 'Справочник контрагентов'
        verbose_name_plural = 'Справочники контрагентов'


class Lot(models.Model):
    CURRENCY_CHOICES = [
        ('R', 'RUB'),
        ('U', 'USD'),
        ('E', 'EUR')
    ]
    NDS_CHOICES = [
        ('N', 'Без НДС'),
        ('OE', '18%'),
        ('TZ', '20%')
    ]

    lot_name = models.CharField(
        verbose_name='Наименование лота',
        max_length=255
    )
    customer_code = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name='Код контрагента'

    )
    price = models.DecimalField(
        verbose_name='Начальная стоимость',
        max_digits=15,
        decimal_places=2
    )
    currency_code = models.CharField(
        verbose_name='Валюта',
        max_length=3,
        choices=CURRENCY_CHOICES

    )
    nbs_rate = models.CharField(
        verbose_name='Код НДС',
        max_length=2,
        choices=NDS_CHOICES
    )
    place_delivery = models.CharField(
        verbose_name='Грузополучатель',
        max_length=255
    )
    date_delivery = models.DateField(verbose_name='Дата доставки')

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'
