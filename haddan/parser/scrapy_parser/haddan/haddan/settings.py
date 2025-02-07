from .constants import RESULTS_DIR


BOT_NAME = "haddan"

SPIDER_MODULES = ["haddan.spiders"]
NEWSPIDER_MODULE = "haddan.spiders"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


FEEDS = {
    f'{RESULTS_DIR}/items.csv': {
        'format': 'csv',
        'fields': ['part_number', 'name', 'type', 'href'],
        'overwrite': True
    },
    f'{RESULTS_DIR}/wear.csv': {
        'format': 'csv',
        'fields': ['part_number', 'name', 'type',
                   'href',
                   'owner',
                   'serial_number'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'haddan.pipelines.HaddanItemsPipeline': 300,
    'haddan.pipelines.HaddanWearPipeline': 300,
}

LOG_ENABLED = True
LOG_LEVEL = 'ERROR'
HTTP_CACHE = True
HTTPCACHE_ENABLED = True


SPIDER_SETTINGS = {
       'ItemsSpider': {
           'ItemsSpider': {
               'haddan.pipelines.HaddanItemsPipeline': 300,
           },
       },
       'WearSpider': {
           'WearSpider': {
               'haddan.pipelines.HaddanWearPipeline': 300,
           },
       },
   }
