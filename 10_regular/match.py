#! /usr/bin/python

#尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
import re
print (re.match('www', 'www.runoob.com').span())   #从开头开始匹配
print (re.match('com', 'www.runoob.com'))
