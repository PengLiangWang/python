#! /usr/bin/python

#方法重写
class Parent:
    def myMethod(self):
        a = 100
        print ("call Parent ", a)

class Child(Parent):
    def myMethod(self):
        a = 200
        print ("call Child ", a)

c = Child()
c.myMethod()
