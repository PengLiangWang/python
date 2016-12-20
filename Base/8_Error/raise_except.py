#! /usr/bin/python

#raise语句允许程序员强行引发一个指定的异常
#raise的唯一参数指示要引发的异常。它必须是一个异常实例或异常类（从Exception派生的类）

try:
    print ('AAAAAA')
    raise NameError('Hi, There')
    print ('BBBBBB')    #上句结束, 不打印
except NameError:
    print ('An exception flew by')
    raise  #调用打印异常信息，异常退出 
