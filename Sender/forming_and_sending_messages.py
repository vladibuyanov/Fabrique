import before_work

from core.models import Client
from message import create_message, sent_message


def forming_and_sending_messages(mail_to_sent):
    """
        Формирование и отправка сообщений
    """
    data = {'id': None, 'phone': None, 'text': mail_to_sent.text_of_message}
    # Определение фильтра для поиска клиентов
    choose_filter = mail_to_sent.client_properties_filter
    client_properties = mail_to_sent.client_properties
    # Выбор клиента по коду
    if choose_filter == 'Код мобильного оператора':
        filtered_clients = Client.objects.filter(mobile_operator_code=client_properties)
        sent(filtered_clients, mail_to_sent, data)
    # Выбор клиента по тегу
    else:
        filtered_clients = Client.objects.filter(tag=client_properties)
        sent(filtered_clients, mail_to_sent, data)


def sent(filtered_clients, mail_to_sent, data):
    for filtered_client in filtered_clients:
        phone_number = filtered_client.phone_number
        new_messages = create_message(mail_to_sent, filtered_client)
        data['phone'] = phone_number
        data['id'] = new_messages.id
        sent_message(data)
        return f'Message for {phone_number} was sent'
