import schedule
import datetime

from forming_and_sending_messages import forming_and_sending_messages
from core.models import MailingList


def today_messages():
    messages_to_sent = MailingList.objects.all()
    today_message = list()
    for message_to_sent in messages_to_sent:
        time_to_sent = message_to_sent.date_of_mailing.timetuple()
        message_day = datetime.date(time_to_sent[0], time_to_sent[1], time_to_sent[2])
        today = datetime.date.today()
        if message_day == today:
            today_message.append(message_to_sent)
    return today_message


def zeromin(minutes):
    if minutes < 10:
        return f'0{minutes}'
    return str(minutes)


def main():
    while True:
        messages_to_sent = schedule.every().day.at('00:00').do(today_messages())
        for message_to_sent in messages_to_sent:
            time_to_sent = message_to_sent.date_of_mailing.timetuple()
            message_hours = f'{time_to_sent[3]}:{zeromin(time_to_sent[4])}'
            schedule.every().day.at(message_hours).do(forming_and_sending_messages())
            schedule.clear()


if __name__ == '__main__':
    main()
