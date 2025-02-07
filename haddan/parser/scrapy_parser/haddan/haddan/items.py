import scrapy


class HaddanItem(scrapy.Item):
    part_number = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    href = scrapy.Field()


class HaddanThing(scrapy.Item):
    part_number = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    href = scrapy.Field()
    owner = scrapy.Field()
    serial_number = scrapy.Field()
