import socket
import subprocess
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto(b'111',('127.0.0.1',8090))
while True:
    cmd = sk.recvfrom(1024)[0].decode('utf-8')
    if cmd == 'q': break
    res = subprocess.Popen(cmd,shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    sk.sendto(res.stdout.read()*100,('127.0.0.1',8090))
    sk.sendto(res.stderr.read(),('127.0.0.1',8090))
sk.close()