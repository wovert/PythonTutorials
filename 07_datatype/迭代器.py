# 双下方法
# print([1].__add__([2]))
# print([1]+[2])
 
# 迭代器
# l = [1,2,3]
# 索引
# 循环 for
# for i in l:
#     i
#
# for k in dic:
#     pass
 
 
# list
# dic
# str
# set
# tuple
# f = open()
# range()
# enumerate
# print(dir([]))   #告诉我列表拥有的所有方法
# ret = set(dir([]))&set(dir({}))&set(dir(''))&set(dir(range(10)))
# print(ret)  #iterable
# print('__iter__' in dir(int))
# print('__iter__' in dir(bool))
# print('__iter__' in dir(list))
# print('__iter__' in dir(dict))
# print('__iter__' in dir(set))
# print('__iter__' in dir(tuple))
# print('__iter__' in dir(enumerate([])))
# print('__iter__' in dir(range(1)))
 
# 只要是能被for循环的数据类型 就一定拥有__iter__方法
# print([].__iter__())
# 一个列表执行了__iter__()之后的返回值就是一个迭代器
# print(dir([]))
# print(dir([].__iter__()))
# print(set(dir([].__iter__())) - set(dir([])))
# print([1,'a','bbb'].__iter__().__length_hint__())  #元素个数
# l = [1,2,3]
# iterator = l.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
 
# Iterable  可迭代的    -- > __iter__  #只要含有__iter__方法的都是可迭代的
# [].__iter__() 迭代器  -- > __next__  #通过next就可以从迭代器中一个一个的取值
 
# 只要含有__iter__方法的都是可迭代的 —— 可迭代协议
 
# print('__iter__' in dir( [].__iter__()))
# print('__next__' in dir( [].__iter__()))
from collections import Iterable
from collections import Iterator
# print(isinstance([],Iterator))
# print(isinstance([],Iterable))
 
# class A:
#     # def __iter__(self):pass
#     def __next__(self):pass
#
# a = A()
# print(isinstance(a,Iterator))
# print(isinstance(a,Iterable))
 
 
# l = [1,2,3,4]
# for i in l.__iter__():
#     print(i)
 
# 迭代器的概念
# 迭代器协议 —— 内部含有__next__和__iter__方法的就是迭代器
 
# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都有__iter__方法
# 只要是迭代器 一定可迭代
# 可迭代的.__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值
 
# for循环其实就是在使用迭代器
# iterator
# 可迭代对象
# 直接给你内存地址
# print([].__iter__())
# print(range(10))
 
#for
#只有 是可迭代对象的时候 才能用for
#当我们遇到一个新的变量，不确定能不能for循环的时候，就判断它是否可迭代
 
# for i in l:
#     pass
#iterator = l.__iter__()
#iterator.__next__()
 
#迭代器的好处：
    # 从容器类型中一个一个的取值，会把所有的值都取到。
    # 节省内存空间
        #迭代器并不会在内存中再占用一大块内存，
            # 而是随着循环 每次生成一个
            # 每次next每次给我一个
# range
# f
# l = [1,2,3,45]
# iterator = l.__iter__()
# while True:
#     print(iterator.__next__())
 
# print(range(100000000000000))
# print(range(3))
# print(list(range(3)))
# def func():
#     for i in  range(2000000):
#         i = 'wahaha%s'%i
#     return i
 
# 生成器 —— 迭代器
# 生成器函数 —— 本质上就是我们自己写得函数
# 生成器表达式
l = [1,2,3,4,5]
for i in l:
    print(i)
    if i == 2:
        break
 
for i in l:
    print(i)