#-*- coding: utf-8 -*-
import os

file_list = []

def find_dir(p_dir, file_name):
  file_abs_path = os.path.join(p_dir, file_name) # 当前正在处理的文件或目录的绝对路劲
  if os.path.isdir(file_abs_path): # 判断当前的文件是一个目录
    for f in os.listdir(file_abs_path): # 进入目录列出该目录下的所有文件列表
      find_dir(file_abs_path, f) # 递归调用
  else:
    if file_abs_path.endswith(".py"):
      if read_and_find_hello(file_abs_path):
        file_list.append(file_abs_path)

def read_and_find_hello(py_file):
  flag = False
  f = open(py_file)
  while True:
    line = f.readline()
    if line == '':
      break
    elif "用户名" in line:
      flag = True
      break
  f.close()
  return flag

# print(read_and_find_hello("./login.py"))
find_dir("./", "login.py")
print(file_list)