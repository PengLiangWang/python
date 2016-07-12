#! /usr/bin/python


for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(4), repr(x*x*x).rjust(6), end='*')        #rejust(2)左侧填充空格数
    print(repr(x*x*x*x).rjust(8), end='*\n')


