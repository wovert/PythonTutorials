# 闭包：嵌套函数，内部函数调用外部函数的变量
def outer():
  a = 1
  def inner():
    print(a)
  print(inner.__closure__)
outer()