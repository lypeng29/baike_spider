#!/usr/bin/python
# -*- coding: utf-8 -*-

from baike_spider import db_mysql

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.db = db_mysql.database()
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
    
    def output_db(self):
        for data in self.datas:
            # fout.write("<h3>%s (%s)</h3>\r\n" % (data['title'],data['url']))
            # fout.write("<p>%s</p><hr/>\r\n" % data['summary'])
            lastid = self.db.insert("insert into cons(title,url,content) values('%s','%s','%s')" % (data['title'],data['url'],self.db.escape(data['summary'])))
            print(lastid)
        self.db.close()
    

    