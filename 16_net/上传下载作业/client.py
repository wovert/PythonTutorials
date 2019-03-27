import os
import json
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
    #file_path = 'E:\python10\day33\作业.py'
    file_path = input('请输入要上传的文件路径 : ')
    # 告诉对方要上传的文件的名字
    file_name = get_filename(file_path)
    # 读要上传的文件 存成字符串
    with open(file_path,encoding='utf-8') as  f:
        content = f.read()
    dic = {'operate':'upload','filename':file_name,'content':content}
    # 将字符串send给server端
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))
    # server端接收 bytes转码程字符串
    # server端打开文件 写文件
elif num == 2:
    '''下载操作'''
sk.close()