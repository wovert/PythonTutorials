import socket
import subprocess
sk = socket.socket()
sk.connect(('127.0.0.1',8090))
while True:
    cmd = sk.recv(1024).decode('utf-8')
    if cmd == 'q': break
    res = subprocess.Popen(cmd,shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    sk.send(res.stdout.read())
    sk.send(res.stderr.read())
sk.close()