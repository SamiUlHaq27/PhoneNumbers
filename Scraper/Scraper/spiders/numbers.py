import scrapy
from ..items import NumberItem

class NumbersSpider(scrapy.Spider):
    name = "numbers"
    allowed_domains = ["sms24.me"]
    start_urls = ["https://sms24.me/en/numbers"]

    def parse(self, response):
        callouts = response.css("a.callout")
        for callout in callouts:
            item = NumberItem()
            item["number"] = callout.css("div.text-primary::text").get()
            item["country"] = callout.css("h5::text").get()
            item["link"] = callout.css("::attr(href)").get()
            yield item
