# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response)
