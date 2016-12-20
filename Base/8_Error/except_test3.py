#! /usr/bin/python

import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError as err:
        print('cannot open.\n{0}'.format(err))
    else:
        print(arg, 'file has', len(f.readlines()), 'lines')
        f.close()
