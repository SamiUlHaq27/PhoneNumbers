import sqlite3
from . import items


numbers_table = """
    create table if not exists number (
        id          integer primary key autoincrement,
        number      varchar(20),
        country     varchar(20),
        link        varchar(100)
    )
"""

messages_table = """
    create table if not exists message (
        id          integer primary key autoincrement,
        number      varchar(20),
        time        varchar(100),
        sender      varchar(50),
        content     text
    )
"""

class database:

    con = None
    cur = None

    def __init__(self, name:str) -> sqlite3.Connection:
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()
        print(sqlite3.sqlite_version, f"Database {name} connected")

    def insert_number(self, item:items.NumberItem):
        
        res = self.cur.execute(f"""select * from number where number = '{item["number"]}'""")

        if len(res.fetchall()) == 0:
            self.cur.execute(f"""
                insert into number (number, country, link)
                values ('{item["number"]}','{item["country"]}','{item["link"]}')
            """)
        else:
            raise Exception("Number already exists")
    
    def insert_message(self, item:items.MessageItem):
        res = self.cur.execute(f"""select * from message where number = '{item["number"]}' and content = '{item["message"]}'""")
        
        if len(res.fetchall()) == 0:
            self.cur.execute("""
                insert into message (number, time, sender, content)
                values ('{}','{}','{}','{}')
            """.format(item["number"],item["time"],item["sender"],item["message"]))
        else:
            raise Exception("Message already exists")
    

