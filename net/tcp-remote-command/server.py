'''
基于TCP实现远程执行命令
在Server端下发命令
'''

import socket

s = socket.socket()
s.bind(('127.0.0.1', 8090))
s.listen()

con,addr = s.accept()

while True:
  cmd = input('>>>')
  con.send(cmd.encode('GBK'))
  res = con.recv(1024).decode('GBK')
  print(res)

con.close()
s.close()




