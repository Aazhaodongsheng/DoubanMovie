import pymysql
import pymysql.cursors


class Dou(object):

    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='zds', password='zds', db='zds', port=3306)
        self.cursor = self.connect.cursor()
        print("______________数据库连接已建立")

    def process_item(self, item, Spider):
        # 往数据库里面写入数据
        print("--------------正在插入数据")
        self.cursor.execute(
            'insert into movieTable(ranking,movie_name,score,score_num)VALUES ("{}","{}","{}","{}")'.format(item['ranking'], item['movie_name'], item['score'], item['score_num']))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, Spider):
        print("============正在关闭数据库连接")
        self.cursor.close()
        self.connect.close()