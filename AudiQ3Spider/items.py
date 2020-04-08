# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Audiq3SpiderItem(scrapy.Item):
    # 图片分类
    category = scrapy.Field()

    # 图片详情地址
    image_detail_url = scrapy.Field()
