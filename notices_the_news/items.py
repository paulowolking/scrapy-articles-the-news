# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticeItem(scrapy.Item):
    image_url = scrapy.Field()
    notice_link = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    data = scrapy.Field()
    texts_replace = scrapy.Field()
