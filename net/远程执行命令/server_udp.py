import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8090))
msg,addr = sk.recvfrom(1024)
while True:
    cmd = input('cmd : ')
    if cmd == 'q':
        sk.sendto(cmd.encode('utf-8'),addr)
        break
    sk.sendto(cmd.encode('utf-8'),addr)
    print('stdout : ',sk.recvfrom(2048)[0].decode('gbk'))
    print('stderr : ',sk.recvfrom(2048)[0].decode('gbk'))
sk.close()















