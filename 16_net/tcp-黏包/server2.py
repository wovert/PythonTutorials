import socket

s = socket.socket()
s.bind(('127.0.0.1', 8090))
s.listen()

con, addr = s.accept()


# 多个 send小的数据连在一起，会发生黏包现象，是tcp协议内部的优化算法造成的
# 连续使用了send 引起的
res = con.recv(12)

# 优先算法
# 连续的小数据包会被合并到res
print(res) # b'helloegg'

# 阻塞，等待接受客户端信息。
# 客户端关闭socket之后，发送空字符串，即res2 接受b''
res2 = con.recv(12)


# windows 会发送一个空消息
# 第版本有可能直接报错
print(res2) # b''


con.close()
s.close()