username = input('请输入你要注册的用户名：')
password = input('请输入你要注册的密码：')
with open('list_of_info',mode='w',encoding='utf-8') as f:
    f.write('{}\n{}'.format(username,password))
print('恭喜您，注册成功')
lis = []
i = 0
while i < 3:
    usn = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    with open('list_of_info',mode='r+',encoding='utf-8') as f1:
        for line in f1:
            lis.append(line)
    if usn == lis[0].strip() and pwd == lis[1].strip():
        print('登录成功')
        break
    else:print('账号和密码错误')
    i+=1