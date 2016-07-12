#! /usr/bin/python
#! coding=utf-8

import time   


ticks = time.time()
print ("Now time: ", ticks)


localtime = time.localtime(time.time())
print ("Now time: ", localtime)


#格式输出1
asctime = time.asctime(time.localtime(time.time()))
print ("Now time: ", asctime)


#格式输出2
print ("Now time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


