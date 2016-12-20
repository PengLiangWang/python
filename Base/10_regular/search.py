#! /usr/bin/python
#re.search 扫描整个字符串并返回第一个成功的匹配

import re

print(re.search('www', 'www.runoob.com').span())         # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
