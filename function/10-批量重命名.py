import os

#1. 获取要重命名的文件夹 名字
folder_name =  input("请输入要重命名的文件夹:")

#2. 获取制定的文件夹中的所有 文件名字
file_names = os.listdir(folder_name)

#os.chdir(folder_name)

#3. 重命名
for name in file_names:
    print(name)
    old_file_name = folder_name+"/"+name
    new_file_name = folder_name+"/"+"[京东出品]-"+name
    os.rename(old_file_name, new_file_name)
