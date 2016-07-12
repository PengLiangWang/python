#! /usr/bin/python

import re

phone = "2004-959-559  #< 这是一个电话号码"

#删除注释
num = re.sub(r'#.*$', "", phone)   #从#号开始，到结尾替换成空
print ("phone_num: ", num)


num = re.sub(r'\D', "", phone)   # '\D' 代表任何非数字
print ("phone_num: ", num)
