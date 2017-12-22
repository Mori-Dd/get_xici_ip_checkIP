# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ScrapyXiciPipeline(object):
    def process_item(self, item, spider):
        items = {
            'IP':item['IP'],
            '端口':item['PORT'],
            '地址':item['POSTION'],
            '匿名':item['TYPE'],
            '属性':item['ATTR'],
            '速度':item['SPEED'],
            '验证时间':item['LAST_CHECK_TIME']
        }
        MONGO_URL = 'localhost'
        MONGO_DB = 'xici'
        MONGO_TABLE = 'xici_ip'

        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        try:
            if db[MONGO_TABLE].insert(items):
                print('存储到MONGODB成功',items)
        except Exception:
            print('存货到MONGODB错误',items)
        return item
