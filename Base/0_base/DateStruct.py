#! /usr/bin/python

#列表

import sys
print (sys.getdefaultencoding())

L1 = [];
L2 = [5,6,7,5,6,5,8,'c']
L1.append(1);
L1.append(2);
print ('L1:',L1)

print ('L2:',L2)
L1.extend(L2);   #将L2列表加到L1列表之后
print ('L1+L2:', L1)


L1.insert(0, 0)
print ('L1.insert(0,0):', L1)  #在第一个位置上面插入元素 0
L1.insert(len(L1), 8)
print ('L1.insert(len(L1), 8):', L1)  
L1.insert(3, 3)
print ('L1.insert(3,3):', L1)

L1.remove(2)
print ('L1.remove(2):', L1)

L1.pop(1)
print ('L1.pop(1): ', L1)   #删除第二个位置的元素
L1.pop()
print ('L1.pop(): ', L1)    #删除列表的最后一个元素


L3 = [1,2,3,4,5,6,7,8]
print ('L3: ', L3)
L3.clear()
print ('L3.clear(): ', L3)


print ('L1.index(7): ' ,L1.index(7))  #列表中元素为7的位置


print ('L1.count(5): ', L1.count(5))   #列表中5出现的次数
print ('L1.count(c): ',L1.count('c'))   #列表中c出现的次数

print ('L1.pop(): ', L1.pop())
L1.sort()
print ('L1.sort(): ', L1)
L1.reverse()
print ('L1.reverse(): ', L1)


L4 = L1.copy()
L5 = L1[:]
print (L4, L5)   #返回列表的一个浅copy

print ('id[L1] = ',id(L1))
print ('id[L4] = ',id(L4))
print ('id[L5] = ',id(L5))

