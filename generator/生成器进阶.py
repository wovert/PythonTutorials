# def generator():
#     print(123)
#     content = yield 1
#     print('=======',content)
#     print(456)
#     arg = yield 2
#     ''''''
#     yield
# g1 = generator()
# g2 = generator()
# g1.__next__()
# g2.__next__()
# print('***',generator().__next__())
# print('***',generator().__next__())
 
# g = generator()
# ret = g.__next__()
# print('***',ret)
# ret = g.send('hello')   #send的效果和next一样
# print('***',ret)
 
#send 获取下一个值的效果和next基本一致
#只是在获取下一个值的时候，给上一yield的位置传递一个数据
#使用send的注意事项
    # 第一次使用生成器的时候 是用next获取下一个值
    # 最后一个yield不能接受外部的值
 
# 获取移动平均值
# 10 20 30 10
# 10 15 20 17.5
# avg = sum/count
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num    # 10
#         count += 1    # 1
#         avg = sum/count
#
# avg_g = average()
# avg_g.__next__()
# avg1 = avg_g.send(10)
# avg1 = avg_g.send(20)
# print(avg1)
 
#预激生成器的装饰器
# def init(func):   #装饰器
#     def inner(*args,**kwargs):
#         g = func(*args,**kwargs)    #g = average()
#         g.__next__()
#         return g
#     return inner
#
# @init
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num    # 10
#         count += 1    # 1
#         avg = sum/count
#
# avg_g = average()   #===> inner
# ret = avg_g.send(10)
# print(ret)
# ret = avg_g.send(20)
# print(ret)
 
#python 3
# def generator():
#     a = 'abcde'
#     b = '12345'
#     for i in a:
#         yield i
#     for i in b:
#         yield i
# def generator():
#     a = 'abcde'
#     b = '12345'
#     yield from a
#     yield from b
#
# g = generator()
# for i in g:
#     print(i)
 
# send
    # send的作用范围和next一模一样
    # 第一次不能用send
    # 函数中的最后一个yield不能接受新的值
 
# 计算移动平均值的例子
# 预激生成器的装饰器的例子
# yield from
