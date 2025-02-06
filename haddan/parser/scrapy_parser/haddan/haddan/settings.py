import os
from scrapy.utils.project import get_project_settings


BOT_NAME = "haddan"

SPIDER_MODULES = ["haddan.spiders"]
NEWSPIDER_MODULE = "haddan.spiders"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


FEEDS = {
    'results/items.csv': {
        'format': 'csv',
        'fields': ['part_number', 'name', 'type', 'href'],
        'overwrite': True
    },
    'results/wear.csv': {
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
       'SpiderB': {
           'ITEM_PIPELINES': {
               'myproject.pipelines.PipelineB': 200,
           },
       },
   }


def update_settings(settings):
    spider = getattr(settings, 'SPIDER', None)
    if spider:
        settings.setdict(SPIDER_SETTINGS.get(spider.name, {}))


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ['SCRAPY_SETTINGS_MODULE'] = 'haddan.settings'
settings = get_project_settings()
update_settings(settings)
