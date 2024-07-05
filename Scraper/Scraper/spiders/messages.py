import scrapy
from ..pipelines import db_con
from ..items import MessageItem

def get_urls() -> list:
    res = db_con.cur.execute("select link from number limit 5")
    links = []
    for i in res.fetchall():
        links.append(i[0])
    return links

class MessagesSpider(scrapy.Spider):
    name = "messages"
    allowed_domains = ["sms24.me"]
    start_urls = ["https://sms24.me/en/numbers/3197010587774"]

    def parse(self, response):
        dls = response.css("dl")[:-1]
        dts_and_dds = []
        for dl in dls:
            dts_and_dds += dl.xpath("./*")
        messages = []
        for i in range(1,len(dts_and_dds),2):
            messages.append([dts_and_dds[i-1],dts_and_dds[i]])
        for message in messages:
            item = MessageItem()
            # the time is gmt time
            item["time"] = message[0].css("div::attr(data-created)").get()
            item["sender"] = message[1].css("label a::text").get()
            item["message"] = message[1].css("span::text").get()
            item["number"] = "+"+response.url.split("/")[-1]
            yield item

        
