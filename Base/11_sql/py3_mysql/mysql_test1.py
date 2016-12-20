#! /usr/local/python3.4.3/bin/python3

import pymysql

#打开数据库链接
db = pymysql.connect("localhost", "root", "123456", "TestDB")
#root=qtpay, TestDB=orc
#实现远程连接
#db = pymysql.connect(host='192.168.1.46', user='root' ,db='TestDB', passwd='123456' ,port=3306)  失败

#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


#执行Sql
cursor.execute("SELECT VERSION()")


#使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)


db.close()
