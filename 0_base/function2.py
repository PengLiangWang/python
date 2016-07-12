#! /usr/bin/python
#coding=gbk

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
     ok = input(prompt)
     if ok in ('y', 'ye', 'yes'):
         print ('YES');
         return True;
     if ok in ('n', 'no', 'nop', 'nope'):
         print ('NO')
         return False;
     retries = retries - 1
     if retries < 0:
         raise OSError('uncooperative user')
     print(complaint)


ask_ok ('OK to overwrite the file?', 10)   
