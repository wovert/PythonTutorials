#1. 打印功能提示
print("="*50)
print("    名字关系系统 V8.6")
print(" 1:添加一个新的名字")
print(" 2:删除一个名字")
print(" 3:修改一个名字")
print(" 4:查询一个名字")
print(" 5:退出系统")
print("="*50)

names = []#定义一个空的列表用来存储添加的名字

while True:

    #2. 获取用的选择
    num = int(input("请输入功能序号:"))


    #3. 根据用户的选择,执行相应的功能
    if num==1:
        new_name = input("请输入名字:")
        names.append(new_name)
        print(names)
    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        find_name = input("请输入要查询的名字:")
        if find_name in names:
            print("找到了你要找的人")
        else:
            print("查无此人")
    elif num==5:
        break
    else:
        print("您的输入有误,请重新输入")
