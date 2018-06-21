#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
使用方法：1.在主程序中先实例化DB Mysql数据库操作类。
      2.使用方法:db=database()  db.fetch_all("sql")
'''
import pymysql
import logging
logging.basicConfig(filename='database.log', filemode="a", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# DB = "database"
# LOGPATH = 'database.log'
# DBNAME = mod_config.getConfig(DB, 'dbname')
# DBHOST = mod_config.getConfig(DB, 'dbhost')
# DBUSER = mod_config.getConfig(DB, 'dbuser')
# DBPWD = mod_config.getConfig(DB, 'dbpassword')
# DBCHARSET = mod_config.getConfig(DB, 'dbcharset')
# DBPORT = mod_config.getConfig(DB, "dbport")

DBNAME = 'baike'
DBUSER = 'root'
DBPWD = 'root'
DBHOST = '127.0.0.1'
DBCHARSET = 'utf8'
DBPORT = 3306
#数据库操作类
class database:
#注，python的self等于其它语言的this
    def __init__(self, dbname=None, dbhost=None):
        self._logger = logging
        #这里的None相当于其它语言的NULL
        if dbname is None:
            self._dbname = DBNAME
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = DBHOST
        else:
            self._dbhost = dbhost
            
        self._dbuser = DBUSER
        self._dbpassword = DBPWD
        self._dbcharset = DBCHARSET
        self._dbport = int(DBPORT)
        self._conn = self.connectMySQL()
        
        if(self._conn):
            self._cursor = self._conn.cursor()


    #数据库连接
    def connectMySQL(self):
        conn = False
        try:
            conn = pymysql.connect(host=self._dbhost,user=self._dbuser,passwd=self._dbpassword,db=self._dbname,port=self._dbport,charset=self._dbcharset)
        except Exception as data:
            self._logger.error("connect database failed, %s" % data)
            conn = False
        return conn

    #插入数据
    def insert(self, sql):
        res = ''
        if(self._conn):
            try:
                self._cursor.execute(sql)
                insert_id = self._cursor.lastrowid
                self._conn.commit()
                return insert_id
            except Exception as data:
                res = False
                self._logger.warn("query database exception, %s" % data)
        return res

    def escape(self,data):
        return pymysql.escape_string(data)

    #获取查询结果集
    def select(self, sql):
        res = ''
        if(self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as data:
                res = False
                self._logger.warn("query database exception, %s" % data)
        return res

    #获取查询结果集
    def count(self, sql):
        res = ''
        if(self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
                if res:
                    return len(res)
                else:
                    return 0
            except Exception as data:
                self._logger.warn("query database exception, %s" % data)
                return 0

    def query(self, sql):
        flag = False
        if(self._conn):
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception as data:
                flag = False
                self._logger.warn("query database exception, %s" % data)
        # return self._cursor.rowcount
        return flag

    #关闭数据库连接
    def close(self):
        if(self._conn):
            try:
                if(type(self._cursor)=='object'):
                    self._cursor.close()
                if(type(self._conn)=='object'):
                    self._conn.close()
            except Exception as data:
                self._logger.warn("close database exception, %s,%s,%s" % (data, type(self._cursor), type(self._conn)))


# db=database()

# lastid = db.insert("insert into cons(title,content,url) values('biaoti','neirong','http://www.baidu.com')")
# print(lastid)
# cous = db.count("select id from cons")
# print(cous)

# alls = db.select("select * from cons")
# print(alls)

# res = db.update("update cons set title='title' where id=1")
# print(res)
# db.close()
