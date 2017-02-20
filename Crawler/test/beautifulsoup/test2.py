#! /usr/bin/env python
#! coding=utf-8

#遍历文档树
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('index.html'), 'html.parser')

print soup.prettify()
print "*"*100
print


#tag 的.content属性可以将tag的子节点以列表的方式输出
print soup.head
print soup.head.contents
print soup.head.contents[0]


#<p> 按段落
#print soup.body.children
for child in soup.body.children:
    print "11111111111111111111111111111111111111"
    print child


