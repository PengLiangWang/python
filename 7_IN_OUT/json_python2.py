#! /usr/bin/python

import json


data1 = {'b':789, 'c':456, 'a':123}
data2 = {'a':123, 'b':789, 'c':456}

d1 = json.dumps(data1, sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys=True, separators=(',',':'))     #压缩去空格，separators
d4 = json.dumps(data1, sort_keys=True, indent=3, separators=(',',':'))  #空3格

print (d1)
print (d2)
print (d3)
print (d4)

print (d1==d2)
print (d1==d3)


#解python
e1 = json.loads(d1)
print (e1)
print (e1['c'])
