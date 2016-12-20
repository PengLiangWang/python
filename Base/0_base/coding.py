#! /usr/bin/python
#coding=gbk

import sys
print (sys.getdefaultencoding())

def f1(a, L=[]):
   L.append(a)
   return L

def f2(a, L=None):
   if L is None:
      L=[]
   L.append(a)
   return L


# 默认值 
print(f1(1))
print(f1(2))
print(f1(3))
print()

print('*************')
# 不让默认值在随后的调用中共享
print()
print(f2(1))
print(f2(2))
print(f2(3))
