#! /usr/bin/env python
#! coding=utf-8

import re

#以数字分隔
pattern = re.compile(r'\d+')

#分隔开的字符串存放到列表中
a=[]
a=re.split(pattern, 'one1two2three3four44324five')
print a


#返回匹配成功的用于分隔的数字
print re.findall(pattern, 'one1two2three3four44324five')


#返回一个迭代器
for m in re.finditer(pattern,'one1two2three3four4'):
        print m.group(),
