# -*- coding: utf-8 -*-
import scrapy
from AudiQ3Spider.items import Audiq3SpiderItem


class Audiq3Spider(scrapy.Spider):
    name = 'audiq3'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/2951.html']

    def parse(self, response):
        """
        提取图片所属更多url链接
        :param response: 调度第一个请求返回的网页源代码
        :return:
        """
        more_urls = response.xpath('//a[@class="more"]/@href').extract()
        for more_url in more_urls:
            full_more_url = response.urljoin(more_url)
            yield scrapy.Request(
                url=full_more_url,
                callback=self.parse_more_url_page
            )

    def parse_more_url_page(self, response):
        """
        获取图片每种分类中的所有详情url链接
        :param response: 更多网页源代码
        :return:
        """
        # 分类名称
        category = "".join(response.xpath('//div[@class="uibox-title"]/text()').extract()).strip()

        detail_urls = response.xpath('//div[@class="uibox"]//ul/li/a/@href').extract()
        full_detail_urls = list(map(lambda x: response.urljoin(x), detail_urls))
        for full_detail_url in full_detail_urls:
            yield scrapy.Request(
                url=full_detail_url,
                callback=self.get_real_url,
                meta={"category": category}
            )

        # 获取下一页url链接
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if "javascript:void(0);" != next_url:
            full_next_url = response.urljoin(next_url)
            yield scrapy.Request(
                url=full_next_url,
                callback=self.parse_more_url_page
            )

    @staticmethod
    def get_real_url(response):
        """
        获取高清图片url地址
        :param response: 缩略图所属网页源代码
        :return:
        """
        category = response.meta.get("category")
        detail_url = response.xpath(' //img[@id="img"]/@src').extract_first()
        image_detail_url = response.urljoin(detail_url)

        item = Audiq3SpiderItem(
            category=category,
            image_detail_url=image_detail_url
        )

        yield item



