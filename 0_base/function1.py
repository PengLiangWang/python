#! /usr/bin/python
#coding=gbk

def fib1(n):
    a, b = 0, 1
    while a < n:
      print (a, end='--')     #��--��Ϊ�ָ�����ӡ
      a, b = b, a+b
    print()

def fib2(n):
    result = []          #����һ���б�
    a, b= 0,1
    while a<n:
      result.append(a)  #���б��ĩβ���һ��Ԫ��
      a,b=b, a+b
    return result

fib1(100)
f100 = fib2(100)  #���շ���ֵ
print (f100)

print (f100[-3])
print (f100[0])
