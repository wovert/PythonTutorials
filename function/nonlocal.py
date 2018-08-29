a = 1
def outer():
  a = 1
  def inner():
      b = 2
      print(a)
      print('inner')
      def inner2():
        nonlocal a # 声明上层第一层的局部变量
        a += 1
        print('inner2')
      inner2()
  inner()
  print('**a**:', a)

outer()
print('全局：', a)