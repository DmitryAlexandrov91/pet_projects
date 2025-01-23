"""Константы проекта haddan parser."""
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

# Константы url адресов.
API_URL = 'https://haddan.ru/inner/api.php'
LIBRIARY_URL = 'https://www.haddan.ru/thing.php?id='

# Константы директорий, путей.
BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR_NAME = 'downloads'
LOGS_DIR_PATH = BASE_DIR / 'logs'
LOG_FILE_NAME = 'parser.log'
LOG_FILE_PATH = LOGS_DIR_PATH / LOG_FILE_NAME
RESULTS_DIR_NAME = 'results'

# Настройки форматов, константы вычислений.
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
MAX_LOG_SIZE = 10 ** 6
MAX_LOGS_COUNT = 5

# Константы команд.
OUTPUT_PRETTY = 'pretty'
OUTPUT_FILE = 'file'
OUTPUT_TELEGRAM_FILE = 'telf'
OUTPUT_TELEGRAM_TEXT = 'telt'

# Константы для тележки
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
