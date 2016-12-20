#! /usr/bin/python

import re

line = "Cats are sMarter than dogs"


matchObj = re.match(r'(.*) (.*) sMarter (.*) (.*)', line, re.I|re.M)  # I 代表对大小写不敏感, M 多行匹配，影响 ^ 和 $

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
    print ("matchObj.group(3) : ", matchObj.group(3))
    print ("matchObj.group(4) : ", matchObj.group(4))

else:
    print ("No match!!")
