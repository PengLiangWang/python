#! /usr/bin/env python
# encoding=utf-8

#设想，如果我们的 cookie.txt 文件中保存的是某个人登录百度的cookie，那么我们提取出这个cookie文件内容，就可以用以上方法模拟这个人的账号登录百度

import cookielib
import urllib2

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
