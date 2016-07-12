#! /usr/bin/python2.6
#! coding=utf-8

Tn = 0
Sn = []

n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))


for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

#Sn列表中两个数相加的结果，再与第三个相加, 以此类推
Sn  = reduce(lambda x,y : x+y, Sn)
print Sn

