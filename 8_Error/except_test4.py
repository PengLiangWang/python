#! /usr/bin/python


try:
    raise Exception('hello', 'world')     #触发异常
except Exception as inst:
    print (type(inst))
    print (inst)
    print (inst.args)

    x, y = inst.args
    print ('x = ', x)
    print ('type(x) = ', type(x))
    print ('y = ', y)
