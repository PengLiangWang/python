#! /usr/bin/python
#! coding=utf-8

import cx_Oracle
from urllib import urlopen


inputs=[]
inputs.append(open('./0.jpg', 'rb'))
inputs.append(open('./1.jpg', 'rb'))


dbconn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')
dbconn.autocommit = 1    #自动提交


cur = dbconn.cursor()
cur.setinputsizes(blobdoc=cx_Oracle.BLOB)

for input in inputs:
    blobdoc = input.read()
    cur.execute("INSERT INTO blob_tab (ID, BLOBDOC) VALUES(blob_seq.NEXTVAL, :blobdoc)", {'blobdoc':blobdoc})
    input.close()
dbconn.close()

