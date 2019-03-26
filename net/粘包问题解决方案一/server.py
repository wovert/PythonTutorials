import json
import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
dic_len = conn.recv(4)  # 4个字节 数字的大小
dic_len = struct.unpack('i',dic_len)[0]
content = conn.recv(dic_len).decode('utf-8')  # 70
content_dic = json.loads(content)
if content_dic['operate'] == 'upload':
    with open(content_dic['filename'],'wb') as f:
        while content_dic['filesize']:
            file = conn.recv(1024)
            f.write(file)
            content_dic['filesize'] -= len(file)
conn.close()
sk.close()