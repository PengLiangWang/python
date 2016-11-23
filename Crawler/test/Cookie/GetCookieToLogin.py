#! /usr/bin/env python
# encoding=utf-8

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#抓包获取参数
postdata = urllib.urlencode({
                        'authorization':'',
                        'login_username':'wpl',
                        'login_password':'wpl19900307',
                        'login.smsVerifyCode':'',
                        'bodyWidth':'1360',
                        'bodyHeight':'633'
                         })
#登录OA管理系统的URL
loginUrl = 'http://192.168.1.40:8090/seeyon/main.do?method=login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
print result.read()
print "*"*50
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问
gradeUrl = 'http://192.168.1.40:8090/seeyon/main.do?method=main'
#请求访问成绩查询网址
result2 = opener.open(gradeUrl)
#print result2.read()

"""
创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。

登录之后才能访问 http://192.168.1.40:8090/seeyon/main.do?method=main 的网址

现在有问题, 访问不到 gradeUrl 地址
"""
