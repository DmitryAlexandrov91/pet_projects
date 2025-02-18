"""Паук на парсинг всех предметов из библиотеки haddan."""
import scrapy
from scrapy.selector import Selector

from haddan.constants import START_PAGE_URL, THING_TYPE_URL
from haddan.items import HaddanItem


class ItemsSpider(scrapy.Spider):
    '''
    Паук items - парсит адрес
    "https://haddan.ru/inner/api_lib.php?cat=thingtype&t="
    от страницы 0 до 105
    '''
    name = "items"
    allowed_domains = ["haddan.ru"]
    start_urls = [START_PAGE_URL + "100"]

    def parse(self, response):
        items = response.css('item').getall()
        for item in items:
            selector = Selector(text=item)
            part_number = selector.css('::attr(ttid)').get()
            data = {
                'part_number': part_number,
                'name': selector.css('::attr(name)').get(),
                'type': selector.css('::attr(type)').get(),
                'href': THING_TYPE_URL + part_number
            }
            yield HaddanItem(data)
        current_page = int(response.url.split('=')[-1])
        next_page = current_page + 1
        if next_page < 120:
            next_url = START_PAGE_URL + str(next_page)
            yield response.follow(next_url, callback=self.parse)
