import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Константы для директорий/путей.
BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR_NAME = 'temp'
KAPCHA_NAME = 'kapcha.png'
SCREENSHOT_NAME = 'screenshot.png'
PAGE_SOURCE_NAME = 'page_source.html'
KAPCHA_PATH = BASE_DIR / DOWNLOADS_DIR_NAME / KAPCHA_NAME
PAGE_SOURCE_PATH = BASE_DIR / DOWNLOADS_DIR_NAME / PAGE_SOURCE_NAME
SCREENSHOT_PATH = BASE_DIR / DOWNLOADS_DIR_NAME / SCREENSHOT_NAME

# константы адресов.
HADDAN_MAIN_URL = 'https://haddan.ru/'
HADDAN_RESERVE_URL = 'https://www.online-igra.ru/'
MEDITATION_URL = 'https://haddan.ru/room/func/temple.php'
KAPCHA_URL = 'https://haddan.ru/inner/img/gc.php'

# Переменные окружения.
FIRST_CHAR = os.getenv('FIRST_CHAR')
SECOND_CHAR = os.getenv('SECOND_CHAR')
PASSWORD = os.getenv('HADDAN_PASSWORD')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Остальное.
PAUSE_DURATION_SECONDS = 50

# Цена ресурсов поляны
FIELD_PRICES = {
    'Мухожор': 9,
    'Подсолнух': 17,
    'Капустница': 28,
    'Мандрагора': 40,
    'Зеленая массивка': 67,
    'Колючник Черный': 101,
    'Гертаниум': 210
    }
