import argparse


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
    return parser
