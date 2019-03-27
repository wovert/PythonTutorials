import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9090))
while True:
    msg,addr = sk.recvfrom(1024)
    print('来自[%s:%s]的消息--%s'%(addr[0],addr[1],msg.decode('utf-8')))
 
    inp = input('>>>')
    sk.sendto(inp.encode('utf-8'),addr)
 
sk.close()