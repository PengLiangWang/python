#! /usr/bin/python

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


try:
    print ('try')
    raise MyError(2*2)
except MyError as e:
    print ('My exception occurred, value: ', e.value)
    raise
#   raise MyError('oops!')

finally:             #离开try之前, 执行 finally 里面内容
    print ('Goodbye, world!')
