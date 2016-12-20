#! /usr/bin/python2.6
#! coding=utf-8


if __name__ == "__main__":
    from sys import stdout
    filename = raw_input('input a file name:\n')
    fp = open(filename, "w")
    ch = raw_input('input string:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = raw_input('\n')   #等待输入, 不然会无限循环
    fp.close()
