#! /usr/bin/python

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def __repr__(self):
        return 'Person Object name : %s , age : %d' %(self.name,self.age)
if __name__ == '__main__':
    import sys
    p = Person(sys.argv[1], int(sys.argv[2]))
    print (p)
