# 需求
    # 写一个时间同步的服务器
    # 服务端接收请求
    # 按照client端发送的时间格式,将服务器时间转换成对应格式
    # 发送给客户端
import time
import socket
 
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))
while True:
    msg,addr = sk.recvfrom(1024)
    # msg 客户端发送给server端的时间格式 "%Y-%m-%d %H:%M-%S"
    time_format = msg.decode('utf-8')
    time_str = time.strftime(time_format)
    sk.sendto(time_str.encode('utf-8'),addr)
sk.close()