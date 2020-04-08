# -*- coding: utf-8 -*-

# Scrapy settings for AudiQ3Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'AudiQ3Spider'

SPIDER_MODULES = ['AudiQ3Spider.spiders']
NEWSPIDER_MODULE = 'AudiQ3Spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'AudiQ3Spider (+http://www.yourdomain.com)'

# 设置log日志等级
LOG_LEVEL = "WARNING"
# 设置保存log信息的日志文件
LOG_FILE = "spider.log"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/"
              "signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "__ah_uuid=5C38927C-7BA9-498B-9AB2-99E889CAD7CC; fvlid=1551418670466MxefJiWnO4; sessionid=8FD9E428-07E1"
              "-4194-82F0-8793F442901A%7C%7C2019-03-01+13%3A37%3A52.647%7C%7C0; cookieCityId=330100; sessionuid=8FD9E"
              "428-07E1-4194-82F0-8793F442901A%7C%7C2019-03-01+13%3A37%3A52.647%7C%7C0; __ah_uuid_ng=c_8FD9E428-07E1-"
              "4194-82F0-8793F442901A; autoid=b50d3748673726af6f4e04a95f0dd1d8; sessionip=218.95.34.108; area=361128;"
              " ahpau=1; __utmz=1.1586246581.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ahsids=2951_2994_2737"
              "_2735_2731_148; __utma=1.1805939796.1551419067.1586246581.1586328213.3; __utmc=1; Hm_lvt_9924a05a5a75c"
              "af05dbbfb51af638b07=1586246561,1586328218; ahpvno=234; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=158633"
              "6664; v_no=1; visit_info_ad=8FD9E428-07E1-4194-82F0-8793F442901A||132CD81A-3317-4CE4-AECA-EE9A4B76C735"
              "||-1||-1||1; sessionvid=132CD81A-3317-4CE4-AECA-EE9A4B76C735; ref=www.baidu.com%7C0%7C0%7C0%7C2020-04-0"
              "8+17%3A03%3A13.347%7C2020-02-20+11%3A08%3A39.563; ahrlid=15863366640337Mp4zepUHI-1586336697250",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'AudiQ3Spider.middlewares.Audiq3SpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'AudiQ3Spider.middlewares.RandomUADownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'AudiQ3Spider.pipelines.Audiq3SpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 存储图片的路径
IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
