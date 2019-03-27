# def max(a,b):
#     return a if a>b else b
#
# def the_max(x,y,z):  #函数的嵌套调用
#     c = max(x,y)
#     return max(c,z)
#
# print(the_max(1,2,3))
 
#函数的嵌套定义
#内部函数可以使用外部函数的变量
# a = 1
# def outer():
#     a = 1
#     def inner():
#         a = 2
#         def inner2():
#             nonlocal a  #声明了一个上面第一层局部变量
#             a += 1   #不可变数据类型的修改
#         inner2()
#         print('##a## : ', a)
#     inner()
#     print('**a** : ',a)
 
# outer()
# print('全局 ：',a)
 
#nonlocal 只能用于局部变量 找上层中离当前函数最近一层的局部变量
#声明了nonlocal的内部函数的变量修改会影响到 离当前函数最近一层的局部变量
# 对全局无效
# 对局部 也只是对 最近的 一层 有影响
# a = 0
# def outer():
#     # a = 1
#     def inner():
#         # a = 2
#         def inner2():
#             nonlocal a
#             print(a)
#         inner2()
#     inner()
#
# # outer()
 
# def func():
#     print(123)
#
# # func()  #函数名就是内存地址
# func2 = func  #函数名可以赋值
# func2()
#
# l = [func,func2] #函数名可以作为容器类型的元素
# print(l)
# for i in l:
#     i()
 
def func():
    print(123)
 
def wahaha(f):
    f()
    return f           #函数名可以作为函数的返回值
 
qqxing = wahaha(func)   # 函数名可以作为函数的参数
qqxing()