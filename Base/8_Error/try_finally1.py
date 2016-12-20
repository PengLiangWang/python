#! /usr/bin/python

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("division by zero!")
    else:
        print ("result is ", result)
    finally:
        print ("executing finally clause")


divide(1,2)
print ("****************")
divide(2,0)
print ("****************")
divide("2", "1")

#任何情况下都会执行finally子句, 由两个字符串相除引发的 TypeError异常没有被except子句处理，因此在执行finally子句后被重新引发
