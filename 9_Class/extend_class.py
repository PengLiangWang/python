#! /usr/bin/python

class Parent:
    parentAttr = 100

    def __init__(self):
        print ("Parent __init__")    

    def parentMethod(self):
        print ("Call parentMethod")

    
    def setAttr(self, attr):
        Parent.parentAttr = attr


    def getAttr(self):
        print ("property of Parent: ", Parent.parentAttr)


 #定义子类继承父类
class Child(Parent):       
    def __init__(self):
        print ("Child __init__")

    def childMethod(self):
        print ("Call childMethod")

c = Child()       #实例化子类 
c.childMethod()   
c.parentMethod()
c.setAttr(200)
c.getAttr()

print (issubclass(Child, Parent))    #True   判断一个类是否另一个类的子类或子孙类
print (issubclass(Parent, Child))    #False
