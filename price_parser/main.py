"""Основной код проекта price_parser."""
import requests_cache
from bs4 import BeautifulSoup


SPAR_MAIN_URL = 'https://myspar.ru/'
SPAR_SEARCH = 'https://myspar.ru/#search?query='
SPAR_CATALOG_URL = 'https://myspar.ru/catalog/'


session = requests_cache.CachedSession()


def get_spar_search_url(product: str):
    """Подставляет аргумент в url поиска товара spar."""
    url = SPAR_SEARCH + product
    return url


def spar_search(product):
    """Поиск товара в SPAR."""
    url = get_spar_search_url(product)
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_spar_catalog(url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
