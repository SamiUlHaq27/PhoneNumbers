import scrapy
import json
from ..pipelines import db_con
from ..items import MessageItem


def get_urls() -> list[str]:
    with open("start_urls.json","r") as f:
        data = json.load(f)
        urls = data["urls"]
        return urls

def get_number() -> str:
    with open("start_urls.json","r") as f:
        data = json.load(f)
        number = data["number"]
        return number

class MessagesSpider(scrapy.Spider):
    name = "messages"
    allowed_domains = ["sms24.me"]
    start_urls = get_urls()

    def parse(self, response):
        number = get_number()
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
            item["number"] = "+"+number
            yield item

        
