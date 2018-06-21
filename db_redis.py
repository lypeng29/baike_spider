#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis

class MyRedis(object):
    def __init__(self):
        self.__pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
        self.r = redis.Redis(connection_pool=self.__pool)
        # self.pipe = self.__redis.pipeline()

    def _str(self,key,value,expire=None):
        if key is None or value is None:
            return False
        if expire is None:
            self.r.set(key,value)
        else:
            self.r.set(key,value,expire)
        return True

    def _list(self,name,value):
        if name is None or value is None:
            return False
        if isinstance(value,(list,tuple)):
            for v in value:
                self.r.lpush(name,v)
        else:
            self.r.lpush(name,value)


    def main(self):
        # self.pipe.set('yn','666')
        # self.pipe.get('yn')
        # self.pipe.execute()
        
        # string
        # self.r.set('name','nihao')
        # print('name is %s ' % self.r.get('name'))

        # list
        # self._list('newline','nihao')
        # self._list('newline',['nihaoa','wohenhao'])
        # print(self.r.lrange('newline',0,-1))
        
        # self.r.lpush('newline','http://www.a.com')
        # self.r.lpush('newline','http://www.b.com')
        # self.r.lpush('newline','http://www.c.com')
        # self.r.lpush('newline','http://www.d.com')
        # print('first url is %s ' % self.r.rpop('newline'))

        pass

if __name__ == '__main__':
    myobj = MyRedis()
    myobj.main()