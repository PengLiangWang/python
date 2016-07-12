#! /usr/bin/python

import json

obj = [[1,2,3],123,12.3,'abc',{'key1':(1,2,3), 'key2':(4,5,6)}]
encodejson = json.dumps(obj)   #转json
print (repr(obj))
#[[1, 2, 3], 123, 12.3, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}]
print (encodejson)
#[[1, 2, 3], 123, 12.3, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]

print (type(encodejson))    # str类型
#str

decodejson = json.loads(encodejson)   #解析json
print (type(decodejson))   # list类型
#list

print (decodejson[1])
print (decodejson[4]['key2'])
print (decodejson)
#[[1, 2, 3], 123, 12.3, 'abc', {'key1': [1, 2, 3], 'key2': [4, 5, 6]}]
