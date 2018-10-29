# 面向对象的进阶
# 其他常用模块
# ftp作业
 
# class A:pass
# class B(A):pass
# a = A()
# print(isinstance(a,A))
# print(issubclass(B,A))
# print(issubclass(A,B))
 
# 反射 ： 是用字符串类型的名字 去操作 变量
# name = 1
# eval('print(name)')  # 安全隐患
 
# 反射 就没有安全问题
 
# 反射 ： 是用字符串类型的名字 去操作 变量
 
 
# 反射对象中的属性和方法   # hasattr getattr setattr delattr
# class A:
#     def func(self):
#         print('in func')
#
# a = A()
# a.name = 'alex'
# a.age = 63
# # 反射对象的属性
# ret = getattr(a,'name')  # 通过变量名的字符串形式取到的值
# print(ret)
# print(a.__dict__)
# 变量名 = input('>>>')   # func
# print(getattr(a,变量名))
# print(a.__dict__[变量名])
#
# # 反射对象的方法
# a.func()
# ret = getattr(a,'func')
# ret()
#
# class A:
#     price = 20
#     @classmethod
#     def func(cls):
#         print('in func')
# # 反射类的属性
# # A.price
# print(getattr(A,'price'))
#
# # 反射类的方法 ：classmethod staticmethod
# # A.func()
# if hasattr(A,'func'):
#     getattr(A,'func')()
 
#模块
# import my
# 反射模块的属性
# print(my.day)
# print(getattr(my,'day'))
 
# 反射模块的方法
# getattr(my,'wahaha')()
 
# 内置模块也能用
# time
# asctime
# import time
# print(getattr(time,'time')())
# print(getattr(time,'asctime')())
 
# def qqxing():
#     print('qqxing')
# year = 2018
# import sys
# # print(sys.modules['__main__'].year)
# # 反射自己模块中的变量
# # print(getattr(sys.modules['__main__'],'year'))
#
# # 反射自己模块中的函数
# # getattr(sys.modules['__main__'],'qqxing')()
# 变量名 = input('>>>')
# print(getattr(sys.modules[__name__],变量名))
 
# 要反射的函数有参数怎么办?
# print(time.strftime('%Y-%m-%d %H:%M:S'))
# print(getattr(time,'strftime')('%Y-%m-%d %H:%M:S'))
 
# 一个模块中的类能不能反射得到
# import my
# print(getattr(my,'C')())
# if hasattr(my,'name'):
#     getattr(my,'name')
 
# 重要程度半颗星
# setattr  设置修改变量
class A:
    pass
a = A()
setattr(a,'name','nezha')
setattr(A,'name','alex')
print(A.name)
print(a.name)
 
# delattr 删除一个变量
delattr(a,'name')
print(a.name)
delattr(A,'name')
print(a.name)