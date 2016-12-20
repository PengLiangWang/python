#! /usr/bin/python

import Person
import json


p = Person.Person('Peter', 22)


def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

 
def dict2object(d):
    #convert dict to object
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
          
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'),value) for key, value in d.items())
        inst = class_(**args)
    else:
        inst = d
    return inst


d = object2dict(p)
print (d)        
#{'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}


#o = dict2object(d)     #此函数有问题
#print (o)


dump = json.dumps(p,default=object2dict)
print (dump)


#load = json.loads(dump,object_hook = dict2object)
#print (load)

