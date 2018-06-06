#!/usr/bin/python
# -*- coding: utf-8 -*-

from baike_spider import url_manager,html_downloader,html_outputer,html_parser

class MySpider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def main(self):
        url = "https://baike.baidu.com/item/php/9337"
        cont = self.downloader.download(url)
        # print(cont)
        urls,res = self.parser.parse(url,cont)
        print(urls)
        print(res)
if __name__ == '__main__':
    myobj = MySpider()
    myobj.main()