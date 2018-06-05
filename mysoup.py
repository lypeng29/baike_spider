#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re,urllib
from urllib.parse import urlparse

url = "https://baike.baidu.com/item/php/9337"
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#     'Referer' : 'https://baike.baidu.com/item/php/9337'
# }
# html = requests.get(url,headers=headers,timeout=10).content.decode('utf-8')

# if html is not None:
#     fp = open('html.txt','w')
#     fp.write(html)
#     fp.close()

# print(5656)
f = open('html.txt', 'r')
html = f.read()
f.close()


# res = {}
# res['url'] = url
# print(html[:500])
# con = re.match(r'<h2>(.*)</h2>', html)
# print(con)

soup = BeautifulSoup(html, 'html.parser')
# title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
# res['title'] = title_node.get_text()

# summary_node = soup.find('div', class_="lemma-summary")
# res['summary'] = summary_node.get_text()

# print(res.items())

new_urls = set()
links = soup.find_all('a',href=re.compile(r"/item"))
for link in links:
    new_url = link['href']
    # new_urls.add(new_url)

    new_full_url = urllib.parse.urljoin(url, new_url)
    new_urls.add(new_full_url)

print(new_urls)
