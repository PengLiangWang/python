#! /usr/bin/python

import copy

a = [1,2,3,4,['a','b']]   #原始数据

b = a
print ('b = ',b)

c = copy.copy(a)   #和 b = a[:] 相同
print ('c = ' ,c)


d = copy.deepcopy(a)
print ('d = ' ,d)

print ('*' * 50)
a.append(5)  #修改对象a
print ('a = ', a)
print ('b = ', b)
print ('c = ', c)  #浅copy, 只拷贝父对象，不会拷贝对象的内部的子对象(所以a中父对象再变化，就不会影响c，因为指向不同的元素)
print ('d = ', d)


print ('*' * 40)
a[4].append('c')   #修改对象a中的['a', 'b']数组对象
print ('a = ', a)
print ('b = ', b)
print ('c = ', c)  #浅copy，指的同一个元素, a修改， c也会变化(子对象指向的是同一个元素)
print ('d = ', d)

