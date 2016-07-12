#! /usr/bin/python

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    x = len(f.readlines())
    print (type(s), s, x)
    i = int(s.strip())
    print (type(i), i)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
