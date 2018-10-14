# 迭代器 & 生成器

## 迭代器

> 访问集合元素的一种方式，迭代器对象从集合的第一个元素开始访问，直到素有的元素被访问完结束，迭代器只能往前不会后退。不要求事先准备好整个迭代过程中所有的元素，迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。适用于遍历一些巨大的或是无限的集合，比如几个G的文件。

## 迭代器特点

1. 访问者不需要关心迭代器内部的结构，仅需通过 next() 方法不断去取下一个内容
2. 不能随机访问集合中的某个值，只能从头到尾一次访问
3. 访问到一半时不能往回退
4. 便于循环比较大的数据集合，节省内存

## 生成一个迭代器

``` python
nums = iter([1,2,3])
print(nums)
print(nums.__next__()) # 1， Python 2.7 nums.next()
print(nums.__next__()) # 2
print(nums.__next__()) # 3
print(nums.__next__()) # StopIteration
```

## 生成器

> 一个函数调用时返回一个迭代器，那个函数就叫做生成器(generator)，如果函数中包含yield 语法，那这个函数就会变成生成器

- 只要含有 `yield` 关键字的函数都是生成器函数
- `yield` 和 `return` 不能共用且需要卸载函数内
- 只要是生成器函数执行之后得到一个生成器作为返回值
- `生成器.__next__()` 返回生成器执行结果，生成器也是迭代器

## yield 作用

yield 可以是函数中断，并保存中断状态，中断后，代码可以继续往下执行，过一段时间还可以在重新调用这个函数，从上次 yield 的下一句开始执行。

``` python
def cash_out(amount): # 函数是生成器
  while amount > 0:
    amount -= 100
    yield 100
    print("擦，又来取钱了...败家子")

ATM = cash_out(500) # ATM 是迭代器
print(type(ATM)) # <class 'generator'>
print("取到钱 %s 万" ATM.__next__()) # 100万
print("取到钱 %s 万" ATM.__next__()) # 100万
print("取到钱 %s 万" ATM.__next__()) # 100万
print("取到钱 %s 万" ATM.__next__()) # 100万
print("取到钱 %s 万" ATM.__next__()) # 100万

```

## 总结

- 双下方法：很少直接调用，一般通过其他语法触发此方法
- 可迭代的 - 可迭代协议：含有__iter__的方法('__iter__' in dir(数据))
- 可迭代的一定可以被 for 循环
- 迭代器协议：含有__iter__和__next__方法
- 迭代器一定可迭代，可迭代器的通过调用iter()方法就能得到一个迭代器
- 迭代器特点
  - 方便使用，切只能取所有的数据取一次
  - 节省内存空间

- 生成器
  - 生成器的本质就是迭代器
  - 生成器表现形式
    - 生成器函数
    - 生成器表达式
- 生成器函数
  - 含有 yield 关键字的函数就是生成器函数
  - 调用函数之后函数不执行，返回一个生成器
  - 函数外调用next方法时候渠道一个值
  - 直到取完最后一个，在执行next会报错

``` python
def generator():
  for i in range(2000000):
    yield '哈哈哈%s' %i
g = generator() #调用生成器函数得到一个生成器
res = g.__next__() # 每一次执行g.__next__就是从生成器中取值，预示着生成器函数中的代码继续执行
print(res)

num = 0
for i in g:
  num += 1
  if num > 50:
    break
  print(i)

```

- 从生成器中取值的几个方法
  - next 方法
  - for
  - 数据类型的强制转换（占用所有数据的内存）

- send 获取下一个值得效果和 next 基本一样，只是在获取下一个值的时候，给上一个值得位置传递一个数据
  - 第一次使用生成器的时候，用next 获取下一个值
  - 最后一个yield 不能接受外部的值

## 生成器表达式

> 每次只能获取一个数据，不占用太多内存

``` python
g = (i for i in range(10))
print(g)
for i in g:
  print(i)
```

## 列表推导式

> 获取所有数据，占用内存

``` python
egg_list = ['鸡蛋%s' %i for i in range(10)]
print(egg_list)
```

## 各种推导式

[每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]    #遍历之后挨个处理

[满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   #筛选功能

``` python
#30以内所有能被3整除的数
ret = [i for i in range(30) if i%3 == 0]  #完整的列表推导式
g = (i for i in range(30) if i%3 == 0)  #完整的列表推导式
print(ret)

#30以内所有能被3整除的数的平方
ret = [i*i for i in (1,2,3,4) if i%3 == 0]
ret = (i*i for i in range(30) if i%3 == 0)
print(ret)

# 例三:找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
ret = [name for lst in names for name in lst if name.count('e') ==2]
ret = (name for lst in names for name in lst if name.count('e') ==2)
print(ret)
```

## 字典推导式

``` python
# 例一：将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
#{10:'a' , 34:'b'}
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)

# 例二：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
#{'a':10+7,'b':34,'z':3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
print(mcase_frequency)
```

## 集合推导式，自带结果去重功能

``` python
squared = {x**2 for x in [1, -1, 2]}
print(squared)
```

- 各种推导式 ： 生成器 列表 字典 集合
- 遍历操作
- 筛选操作