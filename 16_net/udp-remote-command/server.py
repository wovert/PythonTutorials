'''
基于UDP实现远程执行命令
在Server端下发命令
'''

import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8090))
msg,addr = s.recvfrom(1024)

while True:
  cmd = input('>>>')
  if cmd == 'q':
    break
  s.sendto(cmd.encode('GBK'), addr)
  msg, addr = s.recvfrom(1024)
  print(msg.decode('GBK'))

s.close()



