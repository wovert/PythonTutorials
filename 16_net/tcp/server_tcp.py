import socket

s = socket.socket() # 创建socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 避免服务重启的时候 address already in use
s.bind(('127.0.0.1', 8080)) # 绑定IP和port
s.listen() # 监听

con, addr = s.accept() # 接受连接和请求地址,已经完成了3次握手建立了连接并阻塞(等待客户端请求连接)
print(addr)

while True:

  # data = con.recv(1024) # 接受请求方数据，设置1024整数倍
  # print(data)

  # msg = b'Server Hello'
  # con.send(msg) # 发送给请求方数据，必须传bytes类型

  # data2 = con.recv(1024) # 接受请求方数据，设置1024整数倍
  # print(data2.decode('utf-8'))

  # msg2 = bytes('我已经吃了', encoding='utf-8')
  # con.send(msg2) # 发送给请求方数据，必须传bytes类型

  data = con.recv(1024).decode('utf-8') # 接受客户端请求 1024字节数据并阻塞（直到收到一个客户端发来的消息）
  if data == 'bye':
    break

  print(data)
  info = bytes(input('>>>'), encoding='utf-8')
  con.send(info)

con.close() # 结束监听

s.close() # 结束socket

