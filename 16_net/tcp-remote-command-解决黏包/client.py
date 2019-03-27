import socket
import subprocess

s = socket.socket()
s.connect(('127.0.0.1', 8090))

while True:
  cmd = s.recv(1024).decode('utf-8')
  res = subprocess.Popen(cmd, shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

  # res.stdout.read() 返回bytes类型
  std_out = 'stdout:' + (res.stdout.read()).decode('utf-8')
  std_err = 'stderr:' + (res.stderr.read()).decode('utf-8')

  # 发送数据包大小
  s.send(str(len(std_out) + len(std_err)).encode('utf-8'))

  s.recv(1024)

  # 发送数据
  s.send(std_out.encode('utf-8'))
  s.send(std_err.encode('utf-8'))

s.close()


