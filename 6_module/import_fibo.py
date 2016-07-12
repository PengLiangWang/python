#! /usr/bin/python

import fibo

mk = fibo.fib       #函数赋值为本地变量
mf = fibo.fib2

print (mk(100))
print (mf(100))

print ('fibo.__name__: ',fibo.__name__)
