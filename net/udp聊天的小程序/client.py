import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1',9090)
while True:
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'),addr)
    msg_recv,addr = sk.recvfrom(1024)
    print(msg_recv.decode('utf-8'))
sk.close()