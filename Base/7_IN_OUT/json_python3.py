#! /usr/bin/python

import json

#skipkeys参数默认为False。 dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度
data = {'b':789, 'c':456, (1,2):123}
print (json.dumps(data, skipkeys=True))
