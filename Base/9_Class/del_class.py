#! /usr/bin/python


class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, 'had del')



pt1 = Point()
pt2 = pt1
pt3 = pt2

print (id(pt1), id(pt2), id(pt3)) #打印3个对象的id

#程序结束之前, 自动调用 __del__
