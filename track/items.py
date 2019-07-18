# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    trackNo = scrapy.Field()
    trackOrigin = scrapy.Field()
    trackTarget = scrapy.Field()
    trackTime = scrapy.Field()
    trackStatus = scrapy.Field()