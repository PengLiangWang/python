#! /usr/bin/env python
# encoding=utf-8

#HTTPError的父类是URLError, 根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常


import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    if hasattr(e, "code"):
        print e.code

except urllib2.URLError, e:
    if hasattr(e, "reason"):       #为urlError
        print e.reason
else:
    print "OK"
