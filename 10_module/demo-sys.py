import sys
# print(sys.platform)
# print(sys.version)
 
 
# print(sys.path.clear())
 
 
ret = sys.argv
name = ret[1]
pwd = ret[2]
if name == 'alex' and pwd == 'alex3714':
    print('登陆成功')
else:
    print("错误的用户名和密码")
    sys.exit()
print('你可以使用计算器了')
 
 
# 有多少个模块 —— 每个模块大概解决得问题
# 把模块中的所有方法敲一遍 —— 写到博客上
 
# 代码作业
# 计算时间差
# 验证码
# 计算器
 
# 默写：
    #  验证码