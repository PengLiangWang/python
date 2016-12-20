#! /usr/bin/python
#! coding = utf-8

import cx_Oracle
import threading

class AsyncBlobInsert(threading.Thread):
    def  __init__(self, cur, input):
        threading.Thread.__init__(self)
        self.cur = cur
        self.input = input
    def run(self):
        blobdoc = self.input.read()
        self.cur.execute("INSERT INTO blob_tab (ID, BLOBDOC) VALUES(blob_seq.NEXTVAL, :blobdoc)", {'blobdoc':blobdoc})
        self.input.close()
        self.cur.close()


inputs = []
inputs.append(open('/home/wpl/python/Crawler/test1/2.jpg', 'rb'))
inputs.append(open('/home/wpl/python/Crawler/test1/3.jpg', 'rb'))

dbconn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver', threaded=True)     #Tell Oracle use OCI_THREADE
dbconn.autocommit = 1        #or  commit after insert into

th = []
for i, input in enumerate(inputs):
    cur = dbconn.cursor()
    cur.setinputsizes(blobdoc=cx_Oracle.BLOB)
    th.append(AsyncBlobInsert(cur, input))
    th[i].start()

for t in th:
    t.join()
