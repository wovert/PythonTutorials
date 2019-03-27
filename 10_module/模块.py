# 内置模块
# 扩展的 django
# 自定义的
 
# 文件
# import demo
# def read():
#     print('my read func')
# demo.read()
# print(demo.money)
# 先从sys.modules里查看是否已经被导入
# 如果没有被导入，就依据sys.path路径取寻找模块
# 找到了就导入
# 创建这个模块的命名空间
# 执行文件，把文件中的名字都放到命名空间里
# import sys
# print(sys.modules.keys())
# print(sys.path)
 
# import time as t
# print(t.time())
 
# oracle
# mysql
# if 数据库 == ‘oracle’：
#     import oracle as db
# elif 数据库 == ‘mysql’：
#     import mysql as db
# # 连接数据库   db.connect
# # 登录认证
# # 增删改查
# # 关闭数据库
 
# import time,sys,os
 
# from time import sleep
# from demo import read
# def read():
#     print('my read')
# read()
 
# import demo
# from demo import 变量名
 
# from demo import money,read
# # print(money)
# # read()
# money = 200
# read()
# from demo import money,read
# # print(money)
# # read()
# money = 200
# read()
 
# from time import *
# # sleep = 10
# sleep(1)
 
# from math import pi
# print(pi)
# pi = 3
# print(pi)
 
# from demo import *
# print(money)
# read()
 
# import demo
# print(demo.money)
 
# 所有的模块导入都应该尽量往上写
    # 内置模块
    # 扩展模块
    # 自定义模块
# 模块不会重复被导入 ： sys.moudles
# 从哪儿导入模块 : sys.path
#import
# import 模块名
    # 模块名.变量名 和本文件中的变量名完全不冲突
# import 模块名 as 重命名的模块名 ： 提高代码的兼容性
# import 模块1，模块2
 
#from import
# from 模块名 import 变量名
    #直接使用 变量名 就可以完成操作
    #如果本文件中有相同的变量名会发生冲突
# from 模块名 import 变量名字 as 重命名变量名
# from 模块名 import 变量名1，变量名2
# from 模块名 import *
    # 将模块中的所有变量名都放到内存中
    # 如果本文件中有相同的变量名会发生冲突
# from 模块名 import * 和 __all__ 是一对
    # 没有这个变量，就会导入所有的名字
    # 如果有all 只导入all列表中的名字
# __name__
# 在模块中 有一个变量__name__，
# 当我们直接执行这个模块的时候，__name__ == '__main__'
# 当我们执行其他模块，在其他模块中引用这个模块的时候，这个模块中的__name__ == '模块的名字'
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# 绿茶 ： 龙井 碧螺春 竹叶青 信阳毛尖 六安瓜片 太平猴魁 安吉白茶
# 白茶 ： 福鼎白茶 银针（100%芽） 白牡丹（一芽一叶） 贡眉（一芽两叶） 寿眉（一芽三叶）
# 黄茶 ： 黄山毛峰 霍山黄芽
# 青茶 ：
    # 乌龙茶 ：铁观音，大红袍
    # 包种 ： 台湾包种 福建包种
# 红茶 ：
    #  闵红 三功夫一小种
        # 正山小种 ： 金骏眉，银骏眉
        # 政和功夫
        # 坦洋功夫
        # 白琳功夫
    #  祁红
    #  滇红
# 黑茶 ：
    # 普洱 —— 云南
    # 安化黑茶 —— 安徽