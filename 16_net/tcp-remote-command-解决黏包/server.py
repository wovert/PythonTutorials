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
  con.send(cmd.encode('utf-8'))

  num = con.recv(1024).decode('utf-8')
  con.send(b'ok')

  '''
  确定接受的数据大小，但多了一次交互
  '''
  print(num)
  res = con.recv(int(num)).decode('utf-8')

  print(res)

con.close()
s.close()




