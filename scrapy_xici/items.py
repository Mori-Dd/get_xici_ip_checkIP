# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class ScrapyXiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #IP
    IP = scrapy.Field()
    #端口
    PORT = scrapy.Field()
    #地址
    POSTION = scrapy.Field()
    #类型
    TYPE = scrapy.Field()
    #属性
    ATTR = scrapy.Field()
    #速度
    SPEED = scrapy.Field()
    #验证时间
    LAST_CHECK_TIME = scrapy.Field()