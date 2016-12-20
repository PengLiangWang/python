#! /usr/bin/env python
#! coding=utf-8


#re.sub(pattern, repl, string[, count])
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'

#每两个字符串, 替换一次, 最后一个参数2，替换次数(缺省为全替换)
print re.sub(pattern, r'\2 \1', s, 2)


#当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换
#首字母大写(title)
def func(m):
    return m.group(1).title()+ ' ' +m.group(2).title()

print re.sub(pattern, func, s)


#返回结果 + 替换次数
print re.subn(pattern, r'\2 \1', s, 2)
