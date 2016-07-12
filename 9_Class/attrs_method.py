#! /usr/bin/python

class JustCounter:
    __privateCount = 0
    publicCount = 0

    def count(self):
         self.__privateCount += 1
         self.publicCount += 1
         print (self.__privateCount)
         self.__count()    #类的内部调用私有方法, 正确
    def __count(self):     #私有方法
         print ("call private_Method")  

counter = JustCounter()
counter.count()
counter.count()

print (counter.publicCount)
#print (counter.__privateCount)   #调用私有属性, 报错
#counter.__count()    #调用私有方法, 报错
print (counter._JustCounter__privateCount)   #Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
