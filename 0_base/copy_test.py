#! /usr/bin/python

#注意, 文件名不能使用copy.py，会和import copy冲突，报错

import copy

jack = ['jack', ['age', 20]]
print (jack)

#浅copy
#tom = jack[:]
tom = jack
#anny = jack.copy()
#anny = list(jack)
anny = copy.copy(jack)


print (jack, tom, anny)

print (id(jack), id(tom), id(anny))     #不同


tom[0] = 'tom'
anny[0] = 'anny'
print (jack, tom, anny)


anny[1][1] = 18              #修改了一个, 其他两个也改变了
print (jack, tom, anny)      #虽然jack, tom, anny是不同的对象， 但是他们的元素2都指向同一个对象

print ([id(x) for x in jack])
print ([id(x) for x in tom])   #原来jack、tom、anny的岁数元素指向的是同一个元素
print ([id(x) for x in anny])


#深copy
tom = copy.deepcopy(jack) 
anny = copy.deepcopy(jack)
print (jack, tom, anny)


tom[0] = 'tom'
anny[0]  = 'anny'
print (jack, tom, anny)


tom[1][1] = 19              #修改了一个， 不会影响到其他两个
print (jack, tom, anny)      


print ([id(x) for x in jack])
print ([id(x) for x in tom])    #原来的三个 岁数 元素指向的不是同一个元素
print ([id(x) for x in anny])



