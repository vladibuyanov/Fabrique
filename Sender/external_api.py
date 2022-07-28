import before_work
import requests

from core.models import Message


def sent_message_func(message_id, token):
    """
        Функция, собирающая сообщение
    """
    url = 'https://probe.fbrq.cloud/v1/send/'

    sent_messages = Message.objects.filter(id_of_client=message_id)
    for sent_message in sent_messages:
        phone_number = str(sent_message.id_of_client)
        text_of_message = str(sent_message.id_of_mailing_list)
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'id': str(message_id),
            'phone': phone_number,
            'text': text_of_message
        }
        try:
            result = requests.post(url=f'{url}{message_id}', headers=header, json=data)
            return result
        except ConnectionError:
            return "Проблемы с внешним Апи"
