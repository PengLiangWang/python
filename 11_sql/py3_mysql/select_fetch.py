#! /usr/local/python3.4.3/bin/python3


import pymysql

db = pymysql.connect("localhost", "root", "123456", "TestDB");


cursor = db.cursor()


sql = "select * from employee where age > '%d'" %(20)

try:
    cursor.execute(sql)
    results = cursor.fetchall()  #获取所有记录列表

    for row in results:
        fname = row[0]
        lname = row[1] 
        sex   = row[2]
        age   = row[3]

        print ("fname=%s, lname=%s, sex=%s, age=%d" %(fname, lname, sex, age))
except:
    print ("Error: unable to fetch data")


db.close()
