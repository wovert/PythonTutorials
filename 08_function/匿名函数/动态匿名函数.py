#-*- coding: utf-8 -*-

def test(a, b, func):
  result = func(a, b)
  return result

func_new = input("Please input your instruct:") # lambda x, y: x+y
func_new = eval(func_new) # 字符串转换成执行表达式
print(test(22, 33, func_new))