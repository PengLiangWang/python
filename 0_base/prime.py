#! /usr/bin/python
# -*- coding: gbk -*-
# ˫б��// ��floor����, �����ڽ�����������
# ������
# ����ϸ��else�Ӿ�����for ѭ���������� if ���
# �� (for) ѭ�������������б��while��ѭ��������Ϊ false��������break �����ֹʱ������ִ��
# n����2��ʱ����ѭ������������ for x in range(2,2)(range(2,2)�ǿյ�) 


for n in range(2,20):
 for x in range(2, n):
  if(n%x == 0):
   print ('n=', n)
   print ('x=', x)
   print (n,'equal', x, '*' , n//x)
   break
 else:
  print (n, 'is a prime number')
