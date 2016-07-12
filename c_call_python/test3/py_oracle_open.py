#! /usr/bin/python2.6
#! coding=utf-8
import cx_Oracle, json

def DB_connect():
    try:
        conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')
    except cx_Oracle.DatabaseError:
        DataError = "DatabaseError"
        return DataError
    return conn
    

def DB_Open(conn,date):
    DataError = "DatabaseError"
    try:
        cursor = conn.cursor()
        cursor.execute("select * from payjnls where localdate = '%s'" %(date))
    except cx_Oracle.DatabaseError:
         return DataError   
    if conn == DataError:
        return DataError
    return cursor

def DB_fetch(curs):
    one = curs.fetchone()  
    if one == None:
        DataError = "NoneSQL"
        return DataError
    info={}
    info["servcode"]=one[0]
    info["tradecode"]=one[1]
    info["localdate"]=one[2]
    info["localtime"]=one[3]
    info["locallogno"]=one[4]
    JsonStr = json.dumps(info)
    return JsonStr

def connect_close(connt):
    connt.close()
    print "close connect"


def cursor_close(curs):
    curs.close()
    print "close cursor"


if __name__ == "__main__":
     
     connt = DB_connect()
     cur = DB_Open(connt ,'20160510')

     while(True):
         Json = DB_fetch(cur)
         if Json == "NoneSQL":
             break
         print "fetch:",Json
     print "fetch end"
          
     cursor_close(cur)     #关闭游标
     connect_close(connt)  #关闭数据库链接
