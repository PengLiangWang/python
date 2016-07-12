#! /usr/bin/python2.6
import cx_Oracle

def DB_connect():
    DataError = "DatabaseError"
    try:
        conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')
        print "Open Success"
    except cx_Oracle.DatabaseError:
        return DataError
    return conn
    
def DB_close(connt):
    connt.close()
    print "Close Success"


#if __name__ == "__main__":
#    conn = DB_connect()

#    DB_close(conn)
