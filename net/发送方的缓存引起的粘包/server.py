#_*_coding:utf-8_*_
from socket import *
ip_port=('127.0.0.1',8080)

tcp_socket_server=socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)
conn,addr=tcp_socket_server.accept()
data1=conn.recv(10)
data2=conn.recv(10)
print('----->',data1.decode('utf-8'))
print('----->',data2.decode('utf-8'))
conn.close()

