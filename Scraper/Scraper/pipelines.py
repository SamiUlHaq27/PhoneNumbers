# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from . import database
from . import items

db_con = database.database("db.sqlite3")
db_con.cur.execute(database.numbers_table)
db_con.cur.execute(database.messages_table)

class ScraperPipeline:
    def process_item(self, item, spider):
        if type(item) == items.NumberItem:
            db_con.insert_number(item)
        elif type(item) == items.MessageItem:
            db_con.insert_message(item)
        else:
            raise Exception("Wrong item type in pipelines")
        db_con.con.commit()
        return item
