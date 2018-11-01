import os
import json
import struct
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

def get_filename(file_path):
    filename = os.path.basename(file_path)
    return filename

#选择 操作
operate = ['upload','download']
for num,opt in enumerate(operate,1):
    print(num,opt)
num = int(input('请输入您要做的操作序号 : '))
if num == 1:
    '''上传操作'''
    file_path = input('请输入要上传的文件路径 : ')
    file_size = os.path.getsize(file_path)  # 获取文件大小
    file_name = get_filename(file_path)
    dic = {'operate': 'upload', 'filename': file_name,'filesize':file_size}
    str_dic = json.dumps(dic).encode('utf-8')
    ret = struct.pack('i', len(str_dic))  # 将字典的大小转换成一个定长(4)的bytes
    sk.send(ret + str_dic)
    with open(file_path,'rb') as  f:
        while file_size:
            content = f.read(1024)
            sk.send(content)
            file_size -= len(content)
elif num == 2:
    '''下载操作'''
sk.close()