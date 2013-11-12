# Scrapy settings for dirbot project

SPIDER_MODULES = ['sports_tv.spiders']
NEWSPIDER_MODULE = 'sports_tv.spiders'
DEFAULT_ITEM_CLASS = 'sports_tv.items.default.Default'
ITEM_PIPELINES = [
    'sports_tv.pipelines.files_output.FilesOutputPipeline',
]
DOWNLOADER_MIDDLEWARES = {
    #'proxy.ProxyMiddleware': 5,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 10,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 20,
    'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 30,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 40,
}

EXTENSIONS = {
    'scrapy.contrib.debug.StackTraceDump': 10,
    #'scrapy.contrib.throttle.AutoThrottle': 30,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

#ENBALE_PROXY = True
