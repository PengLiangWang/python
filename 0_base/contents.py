#! /usr/bin/python
#coding=gbk

ps = open('test1', 'w')

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


write_multiple_items(ps, '/', '/home', 'wpl','python3','test','test','test.py')
