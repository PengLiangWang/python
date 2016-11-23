#! /usr/bin/env python
# encoding=utf-8

"""
urlopen(url, data, timeout)
    可接收3个参数
    第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
    第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
"""

import urllib2

"""
response = urllib2.urlopen("http://www.baidu.com")
print response.read()
"""

# 其实上面的urlopen参数可以传入一个request请求

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
