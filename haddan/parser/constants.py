"""Константы проекта haddan parser."""
from pathlib import Path


# Константы url адресов.
API_URL = 'https://haddan.ru/inner/api.php'
LIBRIARY_URL = 'https://www.haddan.ru/thing.php?id='

# Константы директорий, путей.
BASE_DIR = Path(__file__).parent
LOGS_DIR_PATH = BASE_DIR / 'logs'
LOG_FILE_NAME = 'parser.log'
LOG_FILE_PATH = LOGS_DIR_PATH / LOG_FILE_NAME

# Настройки форматов, константы вычислений.
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
MAX_LOG_SIZE = 10 ** 6
MAX_LOGS_COUNT = 5