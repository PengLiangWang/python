#! /usr/local/python3.4.3/bin/python3
#! conding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

#设置连接超时时间
s.settimeout(3)

sec = s.gettimeout()
print ("timeout: ", sec)

s.connect((host, port))

msg = s.recv(1024)

#返回连接套接字的远程地址和端口
ipaddr, iport = s.getpeername()
print ("ipaddr: %s, iport: %s" %(ipaddr, iport))

#返回套接字自己的地址和端口
myaddr, myport = s.getsockname()
print ("mypaddr: %s, myport: %s" %(myaddr, myport))


s.close()

print (msg.decode('utf-8'))

#s.setblocking(flag):   如果flag为0, 则将套接字设为非阻塞模式, 否则将套接字设为阻塞模式（默认值）, 非阻塞模式下,如果调用recv()没有发现任何数据,或send()调用无法立即发送数据，那么将引起socket.error异常。
