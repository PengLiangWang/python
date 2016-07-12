#! /usr/bin/python
#! coding=utf-8

#线程优先级队列
#Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
#多线程同步顺序执行队列中的内容

#python2.x中Queue, python3.x中queue
import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print ("Start: "+ self.name)
        process_data(self.name, self.q)
        print ("End: "+ self.name)


def process_data(threadName, q):
    while not exitFlag:
        QueueLock.acquire()
        print ("Thread Lock acquire")
        if not workQueue.empty():
            data = q.get()
            QueueLock.release()
            print ("%s processing %s" %(threadName, data))
            print ("Thread Lock release1")
        else:
            print ("Thread Lock release2")
            QueueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
QueueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1


#创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


#填充队列
QueueLock.acquire()
print ("Main Thread acquire")
for word in nameList:
    workQueue.put(word)
print ("Main Thread release")
QueueLock.release()

#等待队列清空, 队列如果不为空，就一直循环直到队列数据被取完毕
while not workQueue.empty():
    pass


#然后通知线程退出
exitFlag = 1


#再等待所有线程退出完毕, 主线程再退出
for t in threads:
    t.join()

print ("Main Thread End")
