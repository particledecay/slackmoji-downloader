# -*- coding: utf-8 -*-
import scrapy

from downloader.items import EmojiItem


class SlackmojisSpider(scrapy.Spider):
    name = 'slackmojis'
    allowed_domains = ['slackmojis.com']
    start_urls = ['http://slackmojis.com/']

    def parse(self, response):
        for emoji_elem in response.xpath('//li[contains(@class, "emoji")]'):
            emoji = EmojiItem()
            emoji['name'] = emoji_elem.xpath('.//div[@class="name"]/text()').extract()[0]
            emoji['filename'] = emoji_elem.xpath('.//a/@download').extract()[0]
            emoji['url'] = emoji_elem.xpath('.//img/@src').extract()[0]
            yield emoji
