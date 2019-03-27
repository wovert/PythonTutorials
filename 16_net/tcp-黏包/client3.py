import socket
import time

s = socket.socket()
s.connect(('127.0.0.1', 8090))
s.send(b'hello')
time.sleep(0.01)
s.send(b'egg')


s.close()