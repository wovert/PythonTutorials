import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()

conn,addr = sk.accept()
while True:
    cmd = input('cmd : ')
    if cmd == 'q':
        conn.send(cmd.encode('utf-8'))
        break
    conn.send(cmd.encode('utf-8'))
    print('stdout : ',conn.recv(1024).decode('gbk'))
conn.close()
sk.close()















