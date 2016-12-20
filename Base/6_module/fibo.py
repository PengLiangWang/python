#! /usr/bin/python

#让此文件既可以作为可执行的脚本，也可以当作可以导入的模块
#python fibo.py 10(直接传参数，当脚本执行)
#这种方法通常用来为模块提供一个方便的用户接口，或者用来测试


def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end=' ')
        a,b=b,a+b
    print()


def fib2(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b,a+b
    return result
 

if __name__ == "__main__":
     import sys
     fib(int(sys.argv[1]))
