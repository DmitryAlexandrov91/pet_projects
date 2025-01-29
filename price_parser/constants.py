"""Константы проекта price_parser."""
from pathlib import Path


# Директории, пути.
BASE_DIR = Path(__file__).parent
SPAR_MAIN_URL = 'https://myspar.ru/'
SPAR_SEARCH = 'https://myspar.ru/#search?query='
SPAR_CATALOG = 'https://myspar.ru/catalog'
OZON_MAIN_URL = 'https://www.ozon.ru/'
CHROME_DRIVER_PATH = BASE_DIR / 'chromedriver\\chromedriver.exe'