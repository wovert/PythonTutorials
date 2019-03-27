# 超过最大递归限制的报错
# 只要写递归函数，必须要有结束条件。
 
# 返回值
# 不要只看到return就认为已经返回了。要看返回操作是在递归到第几层的时候发生的，然后返回给了谁。
# 如果不是返回给最外层函数，调用者就接收不到。
# 需要再分析，看如何把结果返回回来。
 
# 循环
# 递归
 
 
# 斐波那契  # 问第n个斐波那契数是多少
# 1,1,2,3,5,8   #fib(6) = fib(5) + fib(4)
# def fib(n):
#     if n == 1 or n==2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(50))
 
# fib(6) = fib(5) + fib(4)
# fib(5) = fib(4)+fib(3)
# fib(4) = fib(3)+fib(2)
# fib(3) = fib(2)+fib(1)
# fib(2) = 1
# fib(1) = 1
# def fib(n,l = [0]):
#     l[0] +=1
#     if n ==1 or n == 2:
#         l[0] -= 1
#         return 1,1
#     else:
#         a,b = (n-1)
#         l[0] -= 1
#         if l[0] == 0:
#             return a+b
#         return b,a+b
# print(fib(50))
def fib(n,a=1,b=1):
    if n==1 : return a
    return fib(n-1,b,a+b)
 
print(fib(5))
 
# 阶乘
    #3！ 3*2*1
    # 2! 2*1
    # 1! 1
# def fac(n):
#     if n == 1 :
#         return 1
#     return n * fac(n-1)
#
# print(fac(100))
 
# 附加题 ：考试附加题
    # 递归实现