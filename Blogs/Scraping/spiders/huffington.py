# -*- coding: utf-8 -*-
import scrapy


class HuffingtonSpider(scrapy.Spider):
    name = 'huffington'
    allowed_domains = ['https://www.huffpost.com/news/']
    start_urls = ['https://www.huffpost.com/news/']

    def parse(self, response):
        pass
