#生成器函数
# def generator():
#     print(1)
#     return 'a'
#
# ret = generator()
# print(ret)
 
#只要含有yield关键字的函数都是生成器函数
# yield不能和return共用且需要写在函数内
# def generator():
#     print(1)
#     yield 'a'
# #生成器函数 ： 执行之后会得到一个生成器作为返回值
# ret = generator()
# print(ret)
# print(ret.__next__())
 
# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     yield 'c'
# g = generator()
# for i in g:
#     print(i)
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
 
#娃哈哈%i
def wahaha():
    for i in range(2000000):
        yield '娃哈哈%s'%i
# g = wahaha()
# g1 = wahaha()
# print(g.__next__())
# print(g1.__next__())
 
# g = wahaha()
# count = 0
# for i in g:
#     count +=1
#     print(i)
#     if count > 50:
#         break
# # print('*******',g.__next__())
# for i in g:
#     count +=1
#     print(i)
#     if count > 100:
#         break