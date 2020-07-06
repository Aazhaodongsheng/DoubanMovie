# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


#class DoubanmoviePipeline:
#   def process_item(self, item, spider):
#        return item
class DoubanmoviePipline(object):
    def __init__(self):
        self.connect=pymysql.connect(host='localhost',user='root',password='123456',db='Movie',port=3306)
        self.cursor=self.connect.cursor()
    def process_item(self,item,spider):
        self.cursor.execute('insert into movieTable(raking,movie_name,)')
