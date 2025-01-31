import scrapy
from scrapy.selector import Selector

THING_TYPE_URL = 'https://haddan.ru/thing.php?type='
START_PAGE_URL = "https://haddan.ru/inner/api_lib.php?cat=thingtype&t="


class ItemsSpider(scrapy.Spider):
    name = "items"
    allowed_domains = ["haddan.ru"]
    # start_urls = ["https://haddan.ru/inner/api_lib.php?cat=thingtype&t=0"]
    start_urls = [START_PAGE_URL + "0"]

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
            yield data
        current_page = int(response.url.split('=')[-1])
        next_page = current_page + 1
        if next_page < 105:
            next_url = START_PAGE_URL + str(next_page)
            yield response.follow(next_url, callback=self.parse)
