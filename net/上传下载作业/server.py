import json
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
content = conn.recv(1024).decode('utf-8')
content_dic = json.loads(content)
if content_dic['operate'] == 'upload':
    conn.send(b'received!')
    with open(content_dic['filename'],'wb') as f:
        while content_dic['filesize']:
            file = conn.recv(1024)
            f.write(file)
            content_dic['filesize'] -= len(file)
conn.close()
sk.close()