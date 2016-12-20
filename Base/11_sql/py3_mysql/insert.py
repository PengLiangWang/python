#! /usr/local/python3.4.3/bin/python3
#! coding=utf-8

#! python2用mysqldb

import pymysql

db = pymysql.connect("localhost", "root", "123456", "TestDB");


cursor = db.cursor()


sql="""insert into employee(first_name, last_name, sex, age) values('li', 'qiang', 'nv', 25)"""   #大小写一致


try:
    cursor.execute(sql)
    db.commit()
    print ("Insert Success!")
except:
    print ("Insert Error!")
    db.rollback()


db.close()
