import os
import requests

import before_work
from core.models import Message


def create_message(mail_list_id, client_id):
    """ Создание нового сообщения"""
    new_message = Message(
        id_of_mailing_list=mail_list_id,
        id_of_client=client_id
    )
    new_message.save()
    return new_message


def sent_message(data):
    """ Отправка сообщения """
    url = 'https://probe.fbrq.cloud/v1/send/'
    token = os.getenv('API_TOKEN')
    header = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
    try:
        result = requests.post(url=f'{url}{data["id"]}', headers=header, json=data)
        if result.status_code == 200:
            message_was_sent(data["id"])
        else:
            message_not_sent(data["id"])
        return result

    except ConnectionError:
        return "Проблемы с внешним API"


def message_was_sent(message_id):
    """ Изменение статуса сообщения в случае отправки"""
    message = Message.objects.get(id=message_id)
    message.status = 'Отправлено'
    message.save()


def message_not_sent(message_id):
    """ Изменение статуса сообщения в случае неудачи"""
    message = Message.objects.get(id=message_id)
    message.status = 'Возникла проблема'
    message.save()
