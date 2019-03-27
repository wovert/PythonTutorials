import socket
import subprocess

s = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1', 8090)
s.sendto('吃了吗？'.encode('GBK'), addr)

while True:
  cmd, addr = s.recvfrom(1024)
  res = subprocess.Popen(cmd.decode('GBK'), shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

  # res.stdout.read() 返回bytes类型
  std_out = 'stdout:' + (res.stdout.read()).decode('GBK')
  std_err = 'stderr:' + (res.stderr.read()).decode('GBK')
  s.sendto(std_out.encode('GBK'), addr)
  s.sendto(std_err.encode('GBK'), addr)
s.close()