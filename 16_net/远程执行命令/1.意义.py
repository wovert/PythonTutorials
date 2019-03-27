# server 下发命令
# client 执行命令

# ssh协议
# import os
# ret = os.popen('ls').read()
# print(ret)

import subprocess
# 内置模块 和os模块的功能有相似之处
# 能执行操作系统的命令的功能
ret = subprocess.Popen('dir',    # 要执行的命令
                       shell=True,  # 表示要执行的是一条系统命令
                       stdout=subprocess.PIPE, # 存储执行结果的正常信息
                       stderr=subprocess.PIPE) # 存储执行结果的错误信息
print('stdout : ',ret.stdout.read().decode('gbk'))
print('stderr : ',ret.stderr.read().decode('gbk'))