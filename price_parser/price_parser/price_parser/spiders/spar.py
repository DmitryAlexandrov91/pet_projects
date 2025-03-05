from time import sleep

import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


SPAR_CATALOG_URL = 'https://myspar.ru/'
PAUSE_DURATION_SECONDS = 3


class SparSpider(scrapy.Spider):
    name = "spar"
    allowed_domains = ["myspar.ru"]
    start_urls = ["https://myspar.ru/catalog/"]

    # def __init__(self):
    #     service = Service(executable_path=ChromeDriverManager().install())
    #     driver = webdriver.Chrome(service=service)

    def _parse(self, response):
        service = Service(executable_path=ChromeDriverManager().install())
        # Запуск веб-драйвера для Chrome.
        driver = webdriver.Chrome(service=service)
        driver.get(SPAR_CATALOG_URL)
        driver.maximize_window()
        sleep(PAUSE_DURATION_SECONDS)

