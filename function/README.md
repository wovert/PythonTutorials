# 函数

## print 函数

- 默认输出并换行: `print("string")`
- 指定输出结束符: `print("string", end="__")`

## 自定义函数

``` PYTHON
def func_name():
  ...
  return None
```

- 形式参数(形参)
- 传递参数/实际参数(传参/实参)
- 返回值(注意：返回值得内存地址)
- 函数嵌套调用，必须顺序正确

- 位置参数：必须传值，且有几个参数就传几个传值
- 默认参数：没有传值，使用默认参数

- 形参：
  - `*args`: 元祖
  - `**kargs`: 字典

``` Python
func(1,2,3, a='a',b='b',c='c')
args = (1,2,3)
kargs = {a:'a',b:'b',c:'c'}

li = [1,2,3]
func(*li) # 实参角度，序列按照顺序打散

def func(*args): # 形参角度，给变量加上*，就是组合所有传来的值
'''
#     这个函数实现了什么功能
#     参数1：
#     参数2：
#     :return: 是字符串或者列表的长度
#     '''
```

- 形参：
  - 位置参数 ： 必须传
  - *args ：可以接收任意多个位置参数
  - 默认参数 ： 可以不传
  - **kwargs ： 可以接收多个关键字参数

- 实参：按照位置传参，按照关键字传参

- 默认函数参数的值是一个可变数据类型，那么每一次调用函数的时候，如果不传值就公用这个数据类型的资源

``` python
def fun(k, l={}):
  l[k] = 'v'
  print(l)

fun(1) # {1:'v'}
fun(2) # {1:'v',2:'v'}
fun(3) # {1:'v',2:'v',3:'v'}
```

## 命名空间和作用域

- 内置命名空间
  - Python解释器启动就可以使用的名字存储在内置命名空间中
  - 内置的名字在启动解释器的时候被加载进内存里
    - print()
    - input()
- 全局命名空间
  - 在程序从上到下被执行的过程中一次加载进内存的
  - 放置了我们设置的所有变量名和函数名
- 局部命名空间
  - 函数体内定义的名字
  - 调用函数的时候，才会产生这个名称空间，随着函数执行的结束，这个命名空间就消失

- 在局部:可以使用全局、内置命名空间中的名字
- 在全局:可以使用内置命名空间中的名字，但是不能用局部中使用
- 在内置:不能使用局部和全局的名字的

- globals()
- locals()
- global 关键字

局部调用：局部命名空间 < 全局命名空间 < 内置命名空间

全局调用：全局命名空间 < 内置命名空间

### nonlocal

只能用于局部变量，找上层中离当前函数最近一层的局部变量

声明了 nonlocal 的内部函数的变量修改会影响到里当前函数最近一层的局部变量

对全局无效

对局部也是对最近一层有影响

## return

函数里没有 return, 会默认返回一个 None

如果return多个对象，那么 Python 会把多个对象封装成一个元组作为一个一个整体结果输出

## 作用域

LEGB: Local < Enclosing < Global < Builtin

## 内置函数 Buil-in functions

> 不需要导入模块就可以使用的函数

- abs()
- all([1,2,3,4]) 所有元素都是真的时候返回 True
  - None => False
  - "" => False
  - [] => False
  - () => False
  - {} => False
- any(['',1,{}]) 只有有一个真的则返回 True
- ascii() 返回字符串格式
  - `ascii(8) == int.__repr__()`
- bin(10) # '0b1010'
- bool()
- bytearray("微明", encoding="utf-8") # 返回字节数组 b'\xe5\xbe\xae\xe6\x98\x8e'
- bytes("微明", encoding="utf-8") # 返回字节 b'\xe5\xbe\xae\xe6\x98\x8e'
- callable(变量名) 变量是否可执行函数True
- chr(99) # 'c'
  - `import random`
  - `random.randint(1,99) # 验证码例子`
- ord('c') # 99
- classmethod()
- compile(filename) 编译
  - filename文件的内容字符串编译成python语言
- complex()
- delattr() 反射时使用
- dict()
- dir() 返回列表的key
- divmod()
- enumerate()
  - `li = ['alex','eric','lily']`
  - `for i,item in enumerate(li, 1):print(i,item)`
- eval('6*8')
- exec()
- filter(func, list) 过滤元素
- float()
- format() == int.__format__()`
- frozenset() 不能增加修改set
- getattr()
- globals() 当前所有的全局变量
- hasattr()
- hash()
- help()
- hex()
- id()
- input()
- int()
- isinstance()
- issubclass()
- iter()
- len()
- list()
- locals() 所有的局部变量
- map()
  - li = map(lambda x:x+100, [11,22,33])
  - print(list(li))
- max(1,23,33)
- memoryview()
- min()
- next()
- object()
- oct()
- open()
- pow()
- print()
- property()
- range(0,10) 迭代器，不到10，循环时创建数字
- repr()
- reversed()
- round()
- set()
- setattr()
- slice()
- sorted()
- staticmethod()
- str()
- sum()
- super()
- tuple()
- type()
- vars() 返回key:value
- zip()
- `__import__()`

## 匿名函数-lamda

> `lambda 参数,参数2 : 返回值表达式` 和五个特殊的内置函数可以结合使用

## 递归函数

> 在函数中调用自身函数

- 最大递归深度默认是997/998 —— 是python从内存角度出发做得限制

- 如果递归次数太多，就不适合使用递归来解决问题
- 递归的缺点 ： 占内存
- 递归的优点：  会让代码变简单

RecursionError: maximum recursion depth exceeded while calling a Python object 递归的错误，超过了递归的最大深度