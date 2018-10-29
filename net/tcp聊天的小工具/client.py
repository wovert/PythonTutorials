import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    msg = sk.recv(1024)
    print(msg.decode('utf-8'))
    if msg == b'q':break
    inp = input('>>>')
    if inp == 'q':
        sk.send(inp.encode('utf-8'))
        break
    sk.send(inp.encode('utf-8'))
sk.close()