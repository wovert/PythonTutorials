import socket
 
s = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8082)
msg = '我是客户端'.encode('utf-8')
s.sendto(msg, ip_port)   # 直接给服务器发送一段消息
msg, addr = s.recvfrom(1024)   # 接收对面的回信

content = '\033[34m%s:\033[0m %s'%(addr[0], msg.decode('utf-8'))
print(content)
s.close()