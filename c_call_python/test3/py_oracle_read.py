#! /usr/bin/python2.6


def DB_connect(date, logno):
    import cx_Oracle, json
    try:
        conn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver')
        cursor = conn.cursor()
        cursor.execute("select * from payjnls where localdate = '%s' and locallogno= '%s'" %(date,logno))

    except cx_Oracle.DatabaseError:
         DataError = "DatabaseError"
         return DataError   
    one = cursor.fetchone()  
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
    cursor.close()
    conn.close()
    return JsonStr


#if __name__ == "__main__":

#    Str = DB_connect('201605032','F15332')
#    print type(Str),Str
