# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.exceptions import DropItem
from AudiQ3Spider.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline


class Audiq3SpiderPipeline(ImagesPipeline):

    def __init__(self, *args, **kwargs):
        super(Audiq3SpiderPipeline, self).__init__(*args, **kwargs)
        self.category = None

    def get_media_requests(self, item, info):
        """这个方法是在发送下载请求之前调用，其实该方法本身就是去发送下载请求的"""
        # request_objs = super(Audiq3SpiderPipeline, self).get_media_requests(item, info)
        # for request_obj in request_objs:
        #     request_obj.item = item
        # return request_objs
        self.category = item["category"]

        yield scrapy.Request(item["image_detail_url"])

    def file_path(self, request, response=None, info=None):
        """这个方法是在图片将要被存储时调用，来获取图片存储的路径"""
        path = super(Audiq3SpiderPipeline, self).file_path(request, response, info)
        category_path = os.path.join(IMAGES_STORE, self.category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path, image_name)

        return image_path

    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("图片下载失败！")

        return item


