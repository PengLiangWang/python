#! /usr/bin/python
#! coding=utf-8

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("start: "+ self.name)
        print_time(self.name, self.counter, 5)
        print ("end: "+ self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:    #一直不会执行
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s"%(threadName, time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()   #join等待子线程结束, 主线程才退出

print ("Main Thread end")
