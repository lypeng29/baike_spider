#!/usr/bin/python
# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<!doctype html><html><head><meta charset='utf-8'/><title>baike_spider demo</title></head><body style='padding:20px;width:1200px;margin:0 auto;'>\r\n")
        for data in self.datas:
            fout.write("<h3>%s (%s)</h3>\r\n" % (data['title'],data['url']))
            fout.write("<p>%s</p><hr/>\r\n" % data['summary'])
            
        fout.write("</body></html>")
        fout.close()
    

    