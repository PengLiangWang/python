#! /usr/bin/python


import cx_Oracle

conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')

cursor = conn.cursor()

cursor.execute("select * from TEST_WPL")

one = cursor.fetchone()
print 'ID:%s, COL1:%s, COL2:%s, COL3:%s'%one


#
two = cursor.fetchmany(2)
print two[0], two[1]



three = cursor.fetchall()
for row in three:
      print row


print 'select_by'
cursor.execute("select * from TEST_WPL where ID <= %d" %(2))
#cursor.prepare("select * from TEST_WPL where ID <= :id")
#cursor.execute(None,{'id':2})

for row in cursor:
    print row

cursor.close()
conn.close()


