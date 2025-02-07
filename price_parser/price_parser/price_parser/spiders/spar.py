import scrapy


class SparSpider(scrapy.Spider):
    name = "spar"
    allowed_domains = ["myspar.ru"]
    start_urls = ["https://myspar.ru/catalog/"]

    def parse(self, response):
        categories = response.xpath(
            '//div[@class="catalog-sections"]'
        )
    
