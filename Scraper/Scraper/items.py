# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NumberItem(scrapy.Item):
    country = scrapy.Field()
    number = scrapy.Field()
    link = scrapy.Field()

class MessageItem(scrapy.Item):
    number = scrapy.Field()
    sender = scrapy.Field()
    time = scrapy.Field()
    message = scrapy.Field()
