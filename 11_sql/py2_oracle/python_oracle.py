#! /usr/bin/python

import cx_Oracle

conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')

cursor = conn.cursor () 

sql = """begin
         execute immediate 'DROP TABLE TEST_WPL';
         exception when others then
         null;
         end;"""
cursor.execute(sql)

cursor.execute ("CREATE TABLE TEST_WPL(ID INT, COL1 VARCHAR(32), COL2 VARCHAR(32), COL3 VARCHAR(32))")  
cursor.execute ("INSERT INTO TEST_WPL(ID, COL1, COL2, COL3)VALUES(1, 'a', 'b', 'c')") 
cursor.execute ("INSERT INTO TEST_WPL(ID, COL1, COL2, COL3)VALUES(2, 'aa', 'bb', 'cc')")  
cursor.execute ("INSERT INTO TEST_WPL(ID, COL1, COL2, COL3)VALUES(3, 'aaa', 'bbb', 'ccc')") 
cursor.execute ("INSERT INTO TEST_WPL(ID, COL1, COL2, COL3)VALUES(4, 'aaaa', 'bbbb', 'cccc')") 
conn.commit()  

#one
cursor.execute("SELECT * FROM TEST_WPL")
rows = cursor.fetchall()

for row in rows:
    print "%d, %s, %s, %s" %(row[0], row[1], row[2], row[3])

print "number of rows returned: %d" %cursor.rowcount

#two
cursor.execute("SELECT * FROM TEST_WPL")
while(1):
    row = cursor.fetchone()
    if row  == None:
        break
    print "%d, %s, %s, %s" %(row[0], row[1], row[2], row[3])
print "number of rows returned: %d" %cursor.rowcount

cursor.close() 
conn.close()  
