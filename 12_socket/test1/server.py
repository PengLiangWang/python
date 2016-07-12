#! /usr/local/python3.4.3/bin/python3

import socket, time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(5)


while True:
    #建立客户端连接
    clientsocket,addr = serversocket.accept()
    print ("connect_addr: %s" %str(addr))

    msg ='welcome to www.Baidu.com' + "\r\n"

    time.sleep(2) 
    print ("sleep 2 sec")
    clientsocket.send(msg.encode('utf-8'))

    clientsocket.close()
