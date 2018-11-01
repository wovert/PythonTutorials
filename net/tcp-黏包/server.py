import socket

s = socket.socket()
s.bind(('127.0.0.1', 8090))
s.listen()

con, addr = s.accept()

# 内核空间会缓存b'hello,egg'
res = con.recv(2)
res2 = con.recv(10)

print(res) # b'he'
print(res2) # b'llo,egg'

con.close()
s.close()