#! /usr/bin/python
#! coding = utf-8

import json

#Python字典类型转换为JSON对象

data = {
    'no': 1,
    'name': 'Runoob',
    'url' : 'http://www.runoob.com'
}


json_str = json.dumps(data)

print ("Python data: ", repr(data))
print ("JSON: ", json_str)


#将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

