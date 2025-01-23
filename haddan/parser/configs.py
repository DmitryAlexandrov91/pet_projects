import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import (
    DATETIME_FORMAT, LOG_FORMAT, LOGS_DIR_PATH, LOG_FILE_PATH,
    MAX_LOG_SIZE, MAX_LOGS_COUNT, OUTPUT_FILE, OUTPUT_PRETTY,
    OUTPUT_TELEGRAM_FILE, OUTPUT_TELEGRAM_TEXT
)


def configure_argument_parser(available_modes):
    """Парсер аргументов."""
    parser = argparse.ArgumentParser(description='Парсер шмота персонажей.')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы парсера'
    )
    parser.add_argument(
        'input',
        help='Ник персонажа или id вещи'
    )
    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=(OUTPUT_PRETTY, OUTPUT_FILE,
                 OUTPUT_TELEGRAM_FILE,
                 OUTPUT_TELEGRAM_TEXT),
        help='Дополнительные способы вывода данных'
    )
    return parser


def configure_logging():
    LOGS_DIR_PATH.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE_PATH,
        maxBytes=MAX_LOG_SIZE,
        backupCount=MAX_LOGS_COUNT,
        encoding='utf-8'
    )
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),
    )
