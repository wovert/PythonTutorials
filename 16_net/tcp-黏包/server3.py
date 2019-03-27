import socket

s = socket.socket()
s.bind(('127.0.0.1', 8090))
s.listen()

con, addr = s.accept()

res = con.recv(12)
res2 = con.recv(12)


# 没有黏包
print(res) # b'hello'
print(res2) # b'egg'

con.close()
s.close()