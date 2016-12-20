#! /usr/bin/python
#! coding=utf-8

import sys
import cx_Oracle
import threading
from xml.dom.minidom import parseString

class SyncThread(threading.Thread):
    def __init__(self, cur, query, dom):
        threading.Thread.__init__(self)
        self.cur = cur
        self.query = query[1]  #sql
        print self.query
        self.tag = query[0]
        print self.tag      #test avg, max
        self.dom = dom
    def run(self):
        self.cur.execute(self.query)
        rslt = self.cur.fetchone()[0]
        print rslt       #400,  250
        self.cur.close()
        mutex.acquire()
        sal = self.dom.getElementsByTagName('salary')[0]
        print sal   #salary address
        newtag = self.dom.createElement(self.tag)   #create a neww tag
        newtext = self.dom.createTextNode('%s'%rslt)
        newtag.appendChild(newtext)
        sal.appendChild(newtag)
        mutex.release()


domdoc = parseString('<employees><salary/></employees>')
dbconn = cx_Oracle.connect('qtpay/aaa111@192.168.1.7/dbserver', threaded=True)     #Tell Oracle use OCI_THREADE
mutex = threading.Lock()
queries = {}
queries['avg'] = "SELECT AVG(salary) FROM employees"
queries['max'] = "SELECT MAX(salary) FROM employees"


th = []
for i, query in enumerate(queries.items()):
    cur = dbconn.cursor()
    th.append(SyncThread(cur, query, domdoc))
    th[i].start()


for t in th:
    t.join()


domdoc.writexml(sys.stdout)
print
