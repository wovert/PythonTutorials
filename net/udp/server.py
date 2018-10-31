import socket
sk = socket.socket(type=socket.SOCK_DGRAM)  # 建立一个socket对象, datagram 数据包
# 指定以UDP协议的形式来连接
sk.bind(('127.0.0.1',8080))
# 指定服务的地址
 
msg,addr = sk.recvfrom(1024) # 接收消息,发送端的地址
print(msg,addr)
sk.sendto(b'HELLO',addr)   # 给发送端回复消息
 
sk.close()  # 关闭socket连接