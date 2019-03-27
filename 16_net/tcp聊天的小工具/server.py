import socket
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('192.168.21.36',9000))
sk.listen()
while True:
    conn,addr = sk.accept()  # 接收连接 三次握手conn
    while True:
        inp = input('>>>')
        if inp == 'q':
            conn.send(inp.encode('utf-8'))
            break
        conn.send(inp.encode('utf-8'))
        msg = conn.recv(1024)
        if msg == b'q':break
        print(msg.decode('utf-8'))
    conn.close()    # 四次挥手
sk.close()