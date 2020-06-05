# -*- coding: utf-8 -*-
import scrapy
import html
from datetime import datetime
from Scraping.items import Article


class TmzSpider(scrapy.Spider):
    name = 'tmz'
    allowed_domains = ['https://www.tmz.com/']
    start_urls = ['https://www.tmz.com/']

    def parse(self, response):
        
        blogroll = response.xpath('//*[@class="blogroll"]')
        articles = blogroll.xpath('.//*[@class="article"]')

        for item in articles:

            article = Article (
                id_article = self._generate_id(item),
                title = self._parse_title(item),
                content = self._parse_content(item),
                date = self._parse_date(item),
                link = self._parse_link(item),
            )

            yield article

    def _generate_id(self, item):
        """Generate article id."""
        return ''

    def _parse_title(self, item):
        """Parse article title."""
        h3 = item.xpath('.//*[@class="article__hf1 text-uppercase h3"]/text()').extract_first()
        h3 = h3.strip() + " " if (h3 is not None) else ""
        h1 = item.xpath('.//*[@class="article__hf2 text-uppercase h1"]/text()').extract_first()
        h1 = h1.strip() + " " if (h1 is not None) else ""
        h2 = item.xpath('.//*[@class="article__hf3 text-none h2"]/text()').extract_first()
        h2 = h2.strip() + " " if (h2 is not None) else ""
        
        return h3 + h1 + h2
        #return str(h3).strip() + str(h1).strip() + str(h2).strip()

    def _parse_content(self, item):
        """Parse article content."""
        content = ""
        result = item.xpath('.//*[@class="canvas-block canvas-block-blogroll canvas-text-block canvas-text-block-blogroll canvas-text-block--default  "]/p/text()').extract()
        for p in result:
            content += str(html.unescape(p.strip()))
        return content

    def _parse_date(self, item):
        """Parse article date."""
        date_block = item.xpath('.//*[@class="article__published-at"]/text()')[1].extract().strip()
        date_str = " ".join(date_block.split(" ")[:-1])
        date = datetime.strptime(date_str, '%m/%d/%Y %I:%M %p')

        return date

    def _parse_link(self, item):
        """Parse article link."""
        link = item.xpath('.//*[@class="article__header"]/a/@href').extract_first()
        return link