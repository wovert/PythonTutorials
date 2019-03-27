# client端每隔一段时间发送请求到服务端
# 发送时间的格式
import time
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.sendto('%Y-%m-%d %H:%M:%S'.encode('utf-8'),('127.0.0.1',9000))
msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.close()
 
# 方式一
# 操作系统的定时任务 + python代码的形式
# 方式二
# while True + time.sleep的形式