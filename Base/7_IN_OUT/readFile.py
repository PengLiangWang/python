#! /usr/bin/python

f = open('workfile', 'r')

#print (f.readline())   #read一行，read之后，这一行就没有了 


#print (f.read())  #打印除了第一行外的其他所有行


#for line in f:
#    print(line, end='')

print (f.tell())   #返回当前指向的位置

f.seek(8)

print (f.tell())

print (f.read(1))

f.close()
