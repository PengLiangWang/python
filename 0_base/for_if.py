#! /usr/bin/python
#! coding:gbk


array = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (array)


print ("**************")

combs = []
for x in [1,2,3]:
    for y in [2,3,1]:
        if(x != y):
            combs.append((x,y))

print (combs)
