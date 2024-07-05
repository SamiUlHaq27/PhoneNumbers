"""This file must be put inside main scrapy project folder with scrapy.cfg"""

import json
import os


scraper_path = __file__.replace("runner.py","")

def run_numbers_spider(page_nos:list[int]):
    """`page_nos` is a list of page numbers you want to crawl"""
    os.chdir(scraper_path)
    with open("start_urls.json",'w') as f:
        json.dump({
            "urls":["https://sms24.me/en/numbers/page/{}".format(i) for i in page_nos]
        },f, indent=2)
    os.system("scrapy crawl numbers")

def run_messages_spider(pno:str, page_nos:list[int]):
    """`pno` is the phone number for which you want to crawl messages
    `page_nos` is a list of page numbers you want to crawl"""
    os.chdir(scraper_path)
    pno = pno.replace("+","")
    with open("start_urls.json",'w') as f:
        json.dump({
            "urls":["https://sms24.me/en/numbers/{}/{}".format(pno,i) for i in page_nos],
            "number":pno
        },f,indent=2)
    os.system("scrapy crawl messages")

if __name__=="__main__":
    # run_numbers_spider([2])
    run_messages_spider("+3584573987911",[1,2])