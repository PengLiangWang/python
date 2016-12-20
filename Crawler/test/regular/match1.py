#! /usr/bin/env python
#! coding=utf-8

import re

#匹配如下内容： 单词+空格+单词+任意字符
pattern = re.compile(r'(\w+) (\w+)(.*)')

m = re.match(pattern, 'hello world!')

print "m.string: ", m.string
print "m.groups():", m.groups()
print "m.re: ", m.re

#文本中正则表达式开始搜索的索引
print "m.pos: ", m.pos

#最后一个被捕获的分组在文本中的索引
print "m.lastindex:", m.lastindex

#最后一个被捕获的分组的别名
print "m.lastgroup:", m.lastgroup

print "m.group():", m.group()

print "m.group(1,2):", m.group(1, 2)
                       
print "m.groupdict():", m.groupdict()

#匹配到的第二个字符串开始位置的索引(w的位置)
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)

print "m.start(3):", m.start(3)

#返回start和end的集合
print "m.span(2):", m.span(2)


#任意组合                    
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3') 
