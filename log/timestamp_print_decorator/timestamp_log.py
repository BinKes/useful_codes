# -*- coding: UTF-8 -*-
import time

def timestamp_log(func):
    def wrapper(*args, **kw):
        #print('%s %s():' % (text, func.__name__))
        t1=time.time()
        a = func(*args, **kw)
        t2=time.time()
        print('运行时间：', t2-t1)
        return a
    return wrapper
    