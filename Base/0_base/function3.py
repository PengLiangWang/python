#! /usr/bin/python
#coding=gbk

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

 
parrot(100)
print ()
parrot(1000,action='V0000M')
print ()
parrot('a million', 'bereft of life', 'jump')
print ()
parrot(voltage=5.0, state='dead')   #�����һ��ʹ����keyword�󶨣�����Ķ�����ʹ��keyword��
