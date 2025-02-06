import time

import scrapy
from scrapy.selector import Selector
from selenium import webdriver

from haddan.items import HaddanWear


THING_ID_URL = 'https://www.haddan.ru/thing.php?id='


class WearSpider(scrapy.Spider):
    name = "wear"
    allowed_domains = ["haddan.ru"]

    def __init__(self, *args, **kwargs):
        self.username = kwargs.get('user')
        self.start_urls = [
            f'https://haddan.ru/inner/api.php?op=user&name={self.username}&fields=wear'
        ]
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def parse(self, response):
        wear = response.css('place')
        for thing in wear:
            type = thing.css('place::attr(id)').get()
            serial_number = thing.css('thingid::text').get()
            self.owner = self.username
            href = THING_ID_URL + serial_number
            yield response.follow(
                href, callback=self.parse_wear, cb_kwargs={'type': type})

    def parse_wear(self, response, type):
        self.driver.get(response.url)
        time.sleep(1)
        body = self.driver.page_source
        selector = Selector(text=body)
        thing_name = selector.xpath(
            '//td[@class="description"]/h3/text()'
            ).get()
        part_number = selector.xpath(
            '//span[@class="parC"][contains(text(), "Артикул")]/following-sibling::span[@class="bV"]/text()'
            ).get()
        serial_number = selector.xpath(
            '//span[@class="parC"][contains(text(), "S/N")]/following-sibling::span[@class="bV"]/text()'
            ).get()
        data = {
            'part_number': part_number,
            'name': thing_name,
            'type': type,
            'href': response.url,
            'owner': self.owner,
            'serial_number': serial_number
        }
        yield HaddanWear(data)
