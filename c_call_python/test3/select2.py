#! /usr/bin/python2.6

import cx_Oracle
conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')

def DB_connect(date):
    cursor = conn.cursor()
    cursor.execute("select * from payjnls where localdate >= '%s'" %(date))
    print date, type(date)

    while(1):
        one = cursor.fetchone()  
        if one == None:
            break
        print "servcode: %s, localdate: %s, localtime: %s, locallogno: %s" %(one[0], one[2], one[3], one[4])
    print "number of rows returned: %d" %cursor.rowcount    
    cursor.close()

if __name__ == "__main__":

   curs = DB_connect('20160501')


conn.close()
