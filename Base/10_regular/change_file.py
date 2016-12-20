#! /usr/bin/python

import re

with open('workfile', 'r') as f:
    read_data=f.read()


num = re.sub(r'#.*[e]', "", read_data)
print (num)


with open('workfile1', 'w') as f:
    f.write(num)
