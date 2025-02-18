"""Функции вывода информации проекта haddan parser."""
import logging

from prettytable import PrettyTable
from telebot import apihelper, TeleBot
from tqdm import tqdm

from constants import (
    BASE_DIR, RESULTS_DIR_NAME,
    OUTPUT_FILE, OUTPUT_PRETTY, OUTPUT_TELEGRAM_FILE,
    OUTPUT_TELEGRAM_TEXT,
    TELEGRAM_CHAT_ID, TELEGRAM_TOKEN
)


def control_output(*args):
    commands = {
        OUTPUT_PRETTY: pretty_output,
        OUTPUT_FILE: file_output,
        OUTPUT_TELEGRAM_FILE: telegram_file_output,
        OUTPUT_TELEGRAM_TEXT: telegram_text_output,
        None: default_output
    }
    output = args[1].output
    handler = commands.get(output)
    handler(*args)


def default_output(results, args):
    for row in results:
        print(*row)


def pretty_output(results, args):
    table = PrettyTable()
    table.field_names = [key for key in results.keys()]
    table.align = 'l'
    values = [list(key.items()) for key in results.values()]
    table.add_rows(values)
    # print(table)


def file_output(results, args):
    results_dir = BASE_DIR / RESULTS_DIR_NAME
    results_dir.mkdir(exist_ok=True)

    with open(f'{results_dir}/{args.input}_{args.mode}.txt',
              'w',
              encoding='utf-8') as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    logging.info('Файл с результатами был сохранён.')


def send_message(bot, message):
    """Функция отправки сообщения ботом."""
    try:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message
        )
        logging.debug('Сообщение успешно отправлено в Телеграм.')
    except apihelper.ApiException as error:
        logging.error(f'Ошибка при отправке сообщения:  {error}')
        return False
    else:
        return True


def telegram_file_output(results, args):
    """Отправка в телеграм файла с надетым шмотом персонажа."""
    bot = TeleBot(token=TELEGRAM_TOKEN)
    results_dir = BASE_DIR / RESULTS_DIR_NAME
    results_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{results_dir}/{args.input}_{args.mode}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    with open(filename, 'rb') as f:
        bot.send_document(TELEGRAM_CHAT_ID, f)
    logging.info('Файл с результатами был отправлен в Telegram.')


def telegram_text_output(results, args):
    """Вываливает в телеграм весь обвес юзера."""
    bot = TeleBot(token=TELEGRAM_TOKEN)
    username_message = f'Отправляю шмот игрока {args.input}'
    send_message(bot, username_message)
    for key, value in tqdm(results.items()):
        message_text = f"{key}: {value}"
        send_message(bot, message_text)
