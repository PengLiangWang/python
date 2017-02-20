#! /usr/bin/env python
#! coding=utf-8

def inc(x):
    def incx(y):
        return x + y
    return incx

inc2 = inc(2)     #x=2
inc5 = inc(5)     #x=5

print inc2(5)
print inc5(5)    #y=5
