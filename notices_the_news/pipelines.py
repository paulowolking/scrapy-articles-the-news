# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class SqliteSaveNoticesPipeline:
    def __init__(self):
        self.con = sqlite3.connect('notices_the_news.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS notices(
            image_url TEXT,
            notice_link TEXT,
            title TEXT,
            data TEXT,
            texts_replace BLOB
        )
        """)


    def process_item(self, item, spider):
        self.cur.execute("select * from notices where title = ?", (item['title'],))
        result = self.cur.fetchone()

        if result:
            spider.logger.warn("Item already in database: %s" % item['title'])
        else:
            self.cur.execute("""
                INSERT INTO notices (image_url,notice_link,title,data,texts_replace) VALUES (?, ?, ?, ?, ?)
            """,
            (
                item['image_url'],
                item['notice_link'],
                item['title'],
                item['data'],
                item['texts_replace']
            ))

            self.con.commit()
        
        return item
