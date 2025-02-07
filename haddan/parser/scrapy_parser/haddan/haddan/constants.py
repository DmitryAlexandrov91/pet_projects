"""Константы scrapy парсера haddan."""
from pathlib import Path

THING_TYPE_URL = 'https://haddan.ru/thing.php?type='
START_PAGE_URL = "https://haddan.ru/inner/api_lib.php?cat=thingtype&t="


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR_NAME = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_DIR_NAME
