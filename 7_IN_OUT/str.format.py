#! /usr/bin/python

print ('We are the {} who say "{}!"'.format('knight', 'Ni'))
print ('{0} and {1}'.format('spam', 'eggs'))
print ('{1} and {0}'.format('spam', 'eggs'))
print ('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))


#小数点保留位
import math
print ('The value of PI is approximately {0:.5f}.'.format(math.pi))


# ':'后面紧跟一个整数可以限定该字段的最小宽度。这在美化表格时很有用
table = {'sjoerd': 4127, 'jack': 4098, 'dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10}'.format(name, phone))

#还可以直接传入字典
print ("\n")
table = {'sjoerd': 14127, 'jack': 40298, 'dcab': 76783}
print('jack: {0[jack]}; sjoerd: {0[sjoerd]}; dcab: {0[dcab]}'.format(table))




