#! /usr/bin/python

f = open('testfile', 'w')   #打开文件， 读写操作
for a in range(1,11):
    s=str(a)             #转换成字符串才可以写入文件
    f.write(s)
    f.write('\n')


value=('the answer', 42)
b=str(value)
f.write(b)

f.close()
