#! /usr/bin/python



import cx_Oracle


conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')

cursor = conn.cursor()


cursor.execute("select  * from dual")


row = cursor.fetchone()
print row[0]

cursor.close()
conn.close()
