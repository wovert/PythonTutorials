import socket

s = socket.socket()
s.connect(('127.0.0.1', 8080)) # 建立连接

while True:
  # msg = b'Client Hello'
  # s.send(msg)

  # data = s.recv(1024) # 接受服务端数据
  # print(data)


  # msg2 = bytes('吃饭了吗？', encoding='utf-8')
  # s.send(msg2)

  # data2 = s.recv(1024) # 接受服务端数据
  # print(data2.decode('utf-8'))

  info = bytes(input('>>>'), encoding='utf-8')
  s.send(info)

  data = s.recv(1024).decode('utf-8')
  print(data)
  if data == 'bye':
    s.send(b'bye')
    break

s.close() # 关闭