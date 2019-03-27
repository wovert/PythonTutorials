import socket
import time

s = socket.socket()
s.connect(('127.0.0.1', 8090))
s.send(b'hello')
s.send(b'egg')

time.sleep(5)
s.close()