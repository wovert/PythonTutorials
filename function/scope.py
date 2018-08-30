# 函数进阶

``` PYTHON
a = 1
def func():
  print(a)

func()
```

## 命名空间和作用域

``` python
print()
input()
list
tuple
```
 
## 命名空间 有三种

- 内置命名空间 —— python解释器
  - 就是python解释器一启动就可以使用的名字存储在内置命名空间中
  - 内置的名字在启动解释器的时候被加载进内存里
- 全局命名空间 —— 我们写的代码但不是函数中的代码
  - 是在程序从上到下被执行的过程中依次加载进内存的
  - 放置了我们设置的所有变量名和函数名
- 局部命名空间 —— 函数
  - 就是函数内部定义的名字
  - 当调用函数的时候 才会产生这个名称空间 随着函数执行的结束 这个命名空间就又消失了
 
- 在局部:可以使用全局、内置命名空间中的名字
- 在全局:可以使用内置命名空间中的名字，但是不能用局部中使用
- 在内置:不能使用局部和全局的名字的
 
``` PYTHON
def func():
  a = 1

func()
print(a)
 
def max(l):
  print('in max func')

print(max([1,2,3]))
```

在正常情况下，直接使用内置的名字

当我们在全局定义了和内置名字空间中同名的名字时，会使用全局的名字

当我自己有的时候 我就不找我的上级要了

如果自己没有 就找上一级要 上一级没有再找上一级 如果内置的名字空间都没有 就报错
  多个函数应该拥有多个独立的局部名字空间，不互相共享

``` PYTHON
def input():
  print('in input now')
  def func():
    input = 1
    print(input)
  func()
  def fun1():
    a = 1

  def fun2():pass
```

func  --> 函数的内存地址

函数名() 函数的调用

函数的内存地址() 函数的调用
 
 
## 作用域两种

- 全局作用域 —— 作用在全局 —— 内置和全局名字空间中的名字都属于全局作用域  ——globals()
- 局部作用域 —— 作用在局部 —— 函数（局部名字空间中的名字属于局部作用域） ——locals()
 
``` PYTHON
a = 1
def func():
  global a
  a = 2

func()
print(a)
```

对于不可变数据类型 在局部可是查看全局作用域中的变量

但是不能直接修改

如果想要修改，需要在程序的一开始添加global声明

如果在一个局部（函数）内声明了一个global变量，那么这个变量在局部的所有操作将对全局的变量有效

``` PYTHON
a = 1
b = 2
def func():
  x = 'aaa'
  y = 'bbb'
  print(locals())
  print(globals())

func()
print(globals())
print(locals()) #本地的
```
 
globals 永远打印全局的名字

locals 输出什么 根据locals所在的位置
 
``` PYTHON
a = 1
def func(a):
  a = 2
  return a
a = func(a)
print(a)
```