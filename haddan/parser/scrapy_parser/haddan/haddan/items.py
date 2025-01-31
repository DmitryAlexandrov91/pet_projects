# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HaddanItem(scrapy.Item):
    part_number = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    href = scrapy.Field()
