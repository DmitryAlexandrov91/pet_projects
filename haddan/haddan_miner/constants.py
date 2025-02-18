import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Константы для директорий/путей.
BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR_NAME = 'temp'
KAPCHA_NAME = 'kapcha.png'
PAGE_SOURCE_NAME = 'page_source.html'
KAPCHA_PATH = BASE_DIR / DOWNLOADS_DIR_NAME / KAPCHA_NAME
PAGE_SOURCE_PATH = BASE_DIR / DOWNLOADS_DIR_NAME / PAGE_SOURCE_NAME

# константы адресов.
HADDAN_MAIN_URL = 'https://haddan.ru/'
HADDAN_RESERVE_URL = 'https://www.online-igra.ru/'
MEDITATION_URL = 'https://haddan.ru/room/func/temple.php'
KAPCHA_URL = 'https://haddan.ru/inner/img/gc.php'

# Переменные окружения.
USERNAME = os.getenv('HADDAN_USERNAME')
PASSWORD = os.getenv('HADDAN_PASSWORD')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Остальное.
PAUSE_DURATION_SECONDS = 50
