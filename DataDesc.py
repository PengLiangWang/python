#! /usr/bin/env python
#! coding=utf-8

# 描述符
# instance是类Test的实例, owner是描述符所在的类Test
class NoDataDesc(object):
    def __get__(self, instance, owner):
        print "nodatadesc.attr"
        return instance.freq*2

class DataDesc(object):
    def __get__(self, instance, owner):
        print "datadesc.attr"
        return instance.freq*4 
    
    def __set__(self, instance, value):
        print "set::datadesc.attr"
        print 'freq=%d, value=%d' % (instance.freq, value)
        instance.freq = instance.freq*value

    def __delete__(self, instance):
        print "del datadesc.attr"
        raise BaseException


class Test(object):
    data_result = DataDesc()
    nodata_result = NoDataDesc()    #没有set, 就没有设置值,所以下面self.nodata_result=-1
    def __init__(self, freq, data, nodata):
        self.freq = freq
        self.data_result = data    #先执行描述符NoDataDesc里的set, 再执行get, 获取值
        self.nodata_result = nodata   


test = Test(3, -1, -1)
print test.freq
print test.data_result
print test.nodata_result
