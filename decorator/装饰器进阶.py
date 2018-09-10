#带参数的装饰器
#500个函数
# import time
# FLAGE = False
# def timmer_out(flag):
#     def timmer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 start = time.time()
#                 ret = func(*args,**kwargs)
#                 end = time.time()
#                 print(end-start)
#                 return ret
#             else:
#                 ret = func(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer
# # timmer = timmer_out(FLAGE)
# @timmer_out(FLAGE)    #wahaha = timmer(wahaha)
# def wahaha():
#     time.sleep(0.1)
#     print('wahahahahahaha')
#
# @timmer_out(FLAGE)
# def erguotou():
#     time.sleep(0.1)
#     print('erguotoutoutou')
 
# wahaha()
# erguotou()
 
#多个装饰器装饰一个函数
def wrapper1(func):
    def inner1():
        print('wrapper1 ,before func')
        ret = func()
        print('wrapper1 ,after func')
        return ret
    return inner1
 
def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')
        ret = func()
        print('wrapper2 ,after func')
        return ret
    return inner2
 
def wrapper3(func):
    def inner3():
        print('wrapper3 ,before func')
        ret = func()
        print('wrapper3 ,after func')
        return ret
    return inner3
 
# 从wwrapper1 开始向上装饰， 先执行wrapper1 -> wrapper2 -> wrapper3
@wrapper3
@wrapper2
@wrapper1
def f():
    print('in f')
    return '哈哈哈'
 
print(f())
 
#记录用户的登录情况
#计算这个函数的执行时间