#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
class HtmlDownloader(object):
    
    def download(self, url):
        if url is None:
            return None
        headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Referer' : 'https://baike.baidu.com/item/php/9337'
        }
        response = requests.get(url = url, headers = headers, timeout = 10)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None
    


    