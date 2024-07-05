import scrapy
import json
from ..items import NumberItem

def get_urls() -> list[str]:
    with open("start_urls.json","r") as f:
        data = json.load(f)
        urls = data["urls"]
        return urls

class NumbersSpider(scrapy.Spider):
    name = "numbers"
    allowed_domains = ["sms24.me"]
    start_urls = get_urls()

    def parse(self, response):
        callouts = response.css("a.callout")
        for callout in callouts:
            item = NumberItem()
            item["number"] = callout.css("div.text-primary::text").get()
            item["country"] = callout.css("h5::text").get()
            item["link"] = callout.css("::attr(href)").get()
            yield item
