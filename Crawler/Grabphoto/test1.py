#! /usr/bin/python2.6
#! coding=utf-8
# 获取网页中的图片

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" size'    #python正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg'%x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/4462452095?da_from=ZGFfbGluZT1EVCZkYV9wYWdlPTEmZGFfbG9jYXRlPXAwMDY2JmRhX2xvY19wYXJhbT0xJmRhX3Rhc2s9dGJkYSZkYV9vYmpfaWQ9MjY5MzYmZGFfb2JqX2dvb2RfaWQ9NDcwNzUmZGFfdGltZT0xNDY1OTcwOTI2&da_sign=dd24f5ec93702250200c5d8e93b6ffd5&tieba_from=tieba_da")

print getImg(html)
