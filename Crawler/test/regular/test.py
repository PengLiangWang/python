#! /usr/bin/env python
#! coding=utf-8

__author__ = 'WPL'

#导入 re 模块
import re

#将正则表达式编译成Pattern对象, 注意hello前面的r的意思是"原生字符串"
pattern = re.compile(r'hello')

#使用re.match匹配文本, 获取匹配结果, 无法匹配时将返回None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo wpl')
result3 = re.match(pattern,'helo wpl')
result4 = pattern.match('hello_wpl')   #另一种调用方法

if result1:
    #使用Match获取分组信息
    print result1.group()
else:
    print '1匹配失败'


if result2:
    print result2.group()
else:
    print '2匹配失败'


if result3:
    print result3.group()
else:
    print '3匹配失败'


if result4:
    print result4.group()
else:
    print '4匹配失败'
