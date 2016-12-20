#! /usr/bin/python
#coding=gbk

def fib1(n):
    a, b = 0, 1
    while a < n:
      print (a, end='--')     #以--作为分隔符打印
      a, b = b, a+b
    print()

def fib2(n):
    result = []          #定义一个列表
    a, b= 0,1
    while a<n:
      result.append(a)  #在列表的末尾添加一个元素
      a,b=b, a+b
    return result

fib1(100)
f100 = fib2(100)  #接收返回值
print (f100)

print (f100[-3])
print (f100[0])
