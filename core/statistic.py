from core.models import MailingList, Message


def full_statistic():
    """
        Получение общей статистики по созданным рассылкам
        и количеству отправленных сообщений по ним с группировкой по статусам
    """
    mailing_list_st = MailingList.objects.all()
    count_of_mailing_list = len(mailing_list_st)

    message_st = Message.objects.all()
    count_of_message = len(message_st)
    sent, not_sent, problem = 0, 0, 0
    for message in message_st:
        if message.status == 'Отправлено':
            sent += 1
        elif message.status == 'Не отправлено':
            not_sent += 1
        else:
            problem += 1

    response = {
        'Количество рассылок': count_of_mailing_list,
        'Количество сообщений': count_of_message,
        'Отправленных': sent,
        'Не отправленных': not_sent,
        'С проблемой': problem,
    }

    return response


def detailed_statistics(pk):
    """ Получение детальной статистики отправленных сообщений по конкретной рассылке """
    message_st = Message.objects.filter(id_of_mailing_list=pk, status='Отправлено')
    count_of_sent_message = len(message_st)
    count_of_client = len(set([message.id_of_client for message in message_st]))

    response = {
        'Количество отправленных сообщений': count_of_sent_message,
        'Количество уникальных клиентов': count_of_client
    }

    return response
