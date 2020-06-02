# -*- coding: utf-8 -*-
import scrapy


class TmzSpider(scrapy.Spider):
    name = 'tmz'
    allowed_domains = ['https://www.tmz.com/']
    start_urls = ['https://www.tmz.com/']

    def parse(self, response):
        
        blogroll = response.xpath('//*[@class="blogroll"]')
        articles = blogroll.xpath('.//*[@class="article"]')

        for item in articles:

            article = {
                "id": self._parse_id(item),
                "title": self._parse_title(item),
                "description": self._parse_description(item),
                "date": self._parse_date(item),
                "link": self._parse_link(item),
            }

            yield article

    def _parse_id(self, item):
        pass

    def _parse_title(self, item):
        """Parse article title."""
        return ''

    def _parse_description(self, item):
        pass

    def _parse_date(self, item):
        pass

    def _parse_link(self, item):
        pass