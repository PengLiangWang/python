#! /usr/bin/python
# -*- coding: gbk -*-
# 双斜杠// 是floor除法, 不大于结果的最大整数
# 求质数
# 看仔细：else子句属于for 循环，不属于 if 语句
# 当 (for) 循环迭代完整个列表或（while）循环条件变为 false，而非由break 语句终止时，它会执行
# n等于2的时候，内循环不符合条件 for x in range(2,2)(range(2,2)是空的) 


for n in range(2,20):
 for x in range(2, n):
  if(n%x == 0):
   print ('n=', n)
   print ('x=', x)
   print (n,'equal', x, '*' , n//x)
   break
 else:
  print (n, 'is a prime number')
