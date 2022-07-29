import schedule

from forming_and_sending_messages import forming_and_sending_messages


def main():
    while True:
        schedule.every().day.at('00:00').do(forming_and_sending_messages())


if __name__ == '__main__':
    main()