import socket

# 指定以UDP协议的形式来连接
sk = socket.socket(type=socket.SOCK_DGRAM)  # 建立一个socket对象, datagram 数据包

# 指定服务的地址
sk.bind(('127.0.0.1', 8082))

msg, addr = sk.recvfrom(1024) # 接收消息,发送端的地址

print(addr[0],':', msg.decode('utf-8'))

send_msg = '客户端你好'

sk.sendto(send_msg.encode('utf-8'), addr)   # 给发送端回复消息
 
sk.close()  # 关闭socket连接

# udp 服务不需要监听和建立连接
# 启动服务之后被动的等待客户端发送消息过来
# 客户端发送的消息的同时还会 自带地址信息
# 消息恢复的时候，不仅需要发送消息，还需要把对方的地址填写发送