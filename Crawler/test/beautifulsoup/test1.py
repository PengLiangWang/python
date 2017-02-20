#! /usr/bin/env python
#! coding=utf-8

from bs4 import BeautifulSoup
import bs4

soup = BeautifulSoup(open('index.html'), 'html.parser')

print soup.prettify()

print "*"*100
print "soup.title: ", soup.title
print "soup.title.name: ", soup.title.name
print "soup.title.string: ", soup.title.string


print "*"*100
print "soup.head: ", soup.head
print "soup.head.name: ", soup.head.name


print "*"*100
print "soup.a: ", soup.a
print "soup.a.name: ", soup.a.name
print "type(soup.a.string): ", type(soup.a.string)
if type(soup.a.string) != bs4.element.Comment:   #如果是注释
    print "soup.a.string: ", soup.a.string   #获取标签内部文字


print "*"*100
print "soup.p: ", soup.p    #它查找的是在所有内容中的第一个符合要求的标签
print "soup.p.name: ", soup.p.name
print "soup.p.attrs: ", soup.p.attrs
print "soup.p['class']: ", soup.p['class']
print "soup.p.get('class'): ", soup.p.get('class')

print
print "*************对属性进行修改***************"
print "soup.p['class'] = \"newClass\""
soup.p['class'] = "newClass"
print soup.p


print
print "*************对属性进行删除操作***************"
print "del soup.p['class']"
del soup.p['class']
print soup.p

print 
print "************beautifulSoup当作tag对象***************"
print type(soup.name)
print soup.name 
print soup.attrs
