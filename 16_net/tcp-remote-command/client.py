import socket
import subprocess

s = socket.socket()
s.connect(('127.0.0.1', 8090))

while True:
  cmd = s.recv(1024).decode('GBK')
  res = subprocess.Popen(cmd, shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

  # res.stdout.read() 返回bytes类型
  std_out = 'stdout:' + (res.stdout.read()).decode('GBK')
  std_err = 'stderr:' + (res.stderr.read()).decode('GBK')
  s.send(std_out.encode('GBK'))
  s.send(std_err.encode('GBK'))
s.close()
