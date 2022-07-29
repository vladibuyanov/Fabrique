import datetime

from django.core.validators import RegexValidator
from django.db import models


class MailingList(models.Model):
    """Модель рассылки"""

    class Meta:
        verbose_name = 'Рассылкa'
        verbose_name_plural = 'Рассылки'

    COD_NUMBER = 'Код мобильного оператора'
    TAG = 'Тэг'

    CLIENT_FILTER = [
        (COD_NUMBER, 'Код мобильного оператора'),
        (TAG, 'Тэг')
    ]

    date_of_mailing = models.DateField(
        null=False,
        verbose_name='дата и время запуска рассылки'
    )
    text_of_message = models.TextField(
        null=False,
        verbose_name='текст сообщения для доставки клиенту'
    )
    client_properties_filter = models.CharField(
        max_length=64,
        choices=CLIENT_FILTER,
        verbose_name='Фильтр свойств клиентов'
    )
    client_properties = models.CharField(
        max_length=8,
        verbose_name='Значение выбранного свойства клиента'
    )
    date_of_end_mailing = models.DateField(
        null=False, verbose_name='дата и время окончания рассылки'
    )

    def __str__(self):
        return f'{self.id}//{self.date_of_mailing}'


class Client(models.Model):
    """Модель клиента"""

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    reg_phone_number = RegexValidator(regex=r'^7\w{10}$',
                                      message='номер телефона клиента '
                                      )
    phone_number = models.CharField(max_length=12,
                                    verbose_name='Мобильный телефон',
                                    validators=[reg_phone_number])
    mobile_operator_code = models.IntegerField(
        null=False,
        verbose_name='код мобильного оператора'
    )
    tag = models.CharField(
        unique=False,
        max_length=16,
        verbose_name='тег (произвольная метка)'
    )
    timezone = models.IntegerField(
        verbose_name='часовой пояс'
    )

    def __str__(self):
        return f'{self.id}'


class Message(models.Model):
    """Модель сообщения"""

    class Meta:
        verbose_name = 'Сообщениe'
        verbose_name_plural = 'Сообщения'

    SENT = 'Отправлено'
    NOT_SENT = 'Не отправлено'
    PROBLEM = 'Возникла проблема'
    STATUS = [
        (SENT, 'Отправлено'),
        (NOT_SENT, 'Не отправлено'),
        (PROBLEM, 'Возникла проблема')
    ]

    date_of_create = models.DateField(
        default=datetime.datetime.now(),
        verbose_name='дата и время создания (отправки)',
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=NOT_SENT,
        verbose_name='статус отправки'
    )
    id_of_mailing_list = models.ForeignKey(
        MailingList,
        on_delete=models.CASCADE,
        verbose_name='id рассылки, в рамках которой было отправлено сообщение',
    )
    id_of_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='id клиента',
    )

    def __str__(self):
        return f'Сообщение {self.date_of_create} из {self.id_of_mailing_list}'
