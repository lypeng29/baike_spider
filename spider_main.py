#!/usr/bin/python
# -*- coding: utf-8 -*-

from baike_spider import url_manager,html_downloader,html_outputer,html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_url(root_url)
        while self.urls.has_url():
            try:
                new_url = self.urls.get_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_urls(new_urls)
                # print(new_data)
                self.outputer.collect_data(new_data)
                
                if count == 200:
                    break

                count += 1
            except:
                print('CRAW FAILED')
        self.outputer.output_html()

if __name__=='__main__':
    root_url = "https://baike.baidu.com/item/php/9337"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)