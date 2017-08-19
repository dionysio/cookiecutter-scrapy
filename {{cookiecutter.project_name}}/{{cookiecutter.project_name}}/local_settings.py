from .settings import *

SPIDER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 543,
}


HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'httpcache'

DOWNLOAD_DELAY=1
