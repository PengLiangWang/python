#! /usr/bin/python

def temp_convert(var):
    try:
        return int(var)
 
    except ValueError as Argument:
        print ("The argument does not contain numbers\n", Argument)


p = temp_convert("32")
print (type(p), p)
temp_convert("xyz")
