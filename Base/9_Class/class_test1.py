#! /usr/bin/python

class Employee:
    'All Emplyees Base_Class'     #代码中除了注释, 避免出现中文
    empCount = 0    #类变量
    __empCount = 0   #私有类变量

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):
        print ("Total Employee is ", Employee.empCount)


    def displayEmployee(self):
        print ("Name: ", self.name, ", Salary: ", self.salary)



#创建类的实例, 类的具体对象
emp1 = Employee("wpl", 200000)
#del emp1.salary       #删除某个属性
emp1.salary = 300000   #修改某个对象的属性

#.访问对象的属性(调用对象方法访问属性)
emp1.displayCount()
emp1.displayEmployee()

print ("****************************")
emp2 = Employee("xyx", 15000)
emp2.name="lxx"
emp2.displayCount()
emp2.displayEmployee()


print (hasattr(emp2, 'name'))       #如果存在"name" 属性, 则返回 True
print (getattr(emp2, 'name'))       #获取 "name" 属性的内容
setattr(emp2, 'name', "www")        #设置一个属性。如果属性不存在，会创建一个新属性
print (getattr(emp2, 'name'))       #获取 "name" 属性的内容

#delattr(emp2, 'name')   #删除某个属性

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
