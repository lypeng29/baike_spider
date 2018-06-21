#!/usr/bin/python
# -*- coding: utf-8 -*-

from baike_spider import db_mysql

db=db_mysql.database()

# init_sql = "select url,count(*) as count from cons group by url having count>1"
init_sql = "select content,count(*) as count from cons group by content having count>1 limit 100"
alls = db.select(init_sql)
# print(alls)
# '''
for res in alls:
    # ress = db.select("select id from cons where url='%s'" % res[0])
    ress = db.select("select id from cons where content='%s'" % db.escape(res[0]))
    ids = []
    for i in ress:        
        ids.append(str(i[0]))
    ids.pop()
    newids = ",".join(ids)
    # print(newids)
    devar = db.query("delete from cons where id in (%s)" % newids)
    if devar==False:
        print("delete from cons where id in (%s)" % newids)
    else:
        print(True)

# db.query("delete from cons where content" % newids)
# print(newids)
# '''
