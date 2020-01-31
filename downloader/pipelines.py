# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import errno
import os

import requests
from scrapy.exceptions import DropItem

from downloader import settings


class ColonCleansePipeline(object):
    def process_item(self, item, spider):
        item['name'] = item['name'].strip(':')
        return item


class DownloadPipeline(object):
    def process_item(self, item, spider):
        resp = requests.get(item['url'])
        if resp.status_code >= 400:
            raise DropItem("Received a bad HTTP status for %s: %d" % (item['filename'], resp.status_code))

        if not os.path.isdir(settings.OUTPUT_DIR):
            os.makedirs(settings.OUTPUT_DIR)

        try:
            emoji_file = os.open(os.path.join(settings.OUTPUT_DIR, item['filename']), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except OSError as e:
            if e.errno == errno.EEXIST:
                raise DropItem("Emoji already downloaded: %s" % item['filename'])
            else:
                raise
        
        with os.fdopen(emoji_file, 'wb') as f:
            f.write(resp.content)
        return item