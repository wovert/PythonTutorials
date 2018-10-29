import socket
 
sk = socket.socket(type=socket.SOCK_DGRAM)
 
sk.sendto(b'hello',('127.0.0.1',8080))   # 直接给服务器发送一段消息
msg,addr = sk.recvfrom(1024)   # 接收对面的回信
print(msg)
sk.close()