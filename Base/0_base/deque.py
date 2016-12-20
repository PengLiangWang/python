#! /usr/bin/python
#! coding:gbk

from collections import deque

queue=deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

queue.popleft()

print (queue)

queue.pop()

print (queue)
