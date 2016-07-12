#! /usr/bin/python2.6

from ctypes import *


class point(Structure):           
    _fields_ = [                  
        ("x", c_int),             
        ("y", c_char_p)              
    ]                             

ptr = point(10, 'test')               
libpoint = CDLL("./libpoint.so")  
#libpoint.point_print(byref(ptr))  
libpoint.point_print(pointer(ptr))
