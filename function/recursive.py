import sys

# 设置递归深度，不推荐修改。到达此数值之前结束程序并输出结果没有错误提示
sys.setrecursionlimit(1000000) 

n = 0
def story():
  global n
  n += 1
  print(n)
  story()

story()

#RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归的错误，超过了递归的最大深度

# alex 多大       n = 1   age(1) = age(2)+2 = age(n+1) + 2
# alex比egon大两岁
# egon多大？      n = 2   age(2) = age(3) + 2 = age(n+1) +2
# egon比wusir大两岁
# wusir多大       n = 3   age(3) = age(4) + 2 = age(n+1) +2
# wusir比金老板大两岁
# 金老板多大？
# 金老板40了      n = 4   age(4) = 40
 
# n = 4 age(4) = 40
# n <4  age(n) = age(n+1) +2
def age(n):
    if n == 4:
        return 40
    elif n >0 and n < 4:
        age(n+1) + 2
#
print(age(1))
 
# # 教你看递归
# def age(1):
#     if 1 == 4:
#         return 40
#     elif 1 > 0 and 1 < 4:
#         return 46
#
# def age(2):
#     if 2 == 4:
#         return 40
#     elif 2 >0 and 2 < 4:
#         age(3) + 2    None +2
#
# def age(3):
#     if 3 == 4:
#         return 40
#     elif 3 >0 and 3 < 4:
#         42
#
# def age(4):
#     if 4 == 4:
#         return 40
#     elif n >0 and n < 4:
#         age(n+1) + 2