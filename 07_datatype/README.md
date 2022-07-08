# 数据类型

- 布尔型：`bool`
- 数值: `int`
- 字符串: `str`
- 元组: `tuple`
- 列表: `list`
- 字典: `dict`
- 集合: `set`
- 类类型
- None

- 深浅 `copy`

## 布尔型 bool (不可变类型)

- 值范围：{True, False}

True

```py
bool(1)
bool(0b01))
bool(-1.2)
bool('s')
bool([1])
```

Flase

``` Python
bool(0b0)
bool(0.0)
bool('')
bool("")
bool(None)
bool([])
bool(())
bool({})
```

## 数值

- 整型
  - 整型 int
  - 长整型 long
  - Python 3 里都是整型
- 浮点型

### 整型 int (不可变类型)

- 10进制：{0,9}
- 2进制：{0,1}
  - 表示法：0b10
- 8进制：{0,7}
  - 表示法：0o10
- 16进制：{0,f}
  - 表示法：0xff

- 转换2进制：
  - 10->2 : bin(10)
  - 8->2 : bin(0o10)
  - 16->2 : bin(oxff)
- 转换10进制：
  - 2->10 : int(0b111)
  - 8->10 : int(0o10)
  - 16->10: int(oxff)
- 转换8进制：
  - 2->8 : oct(0b111)
  - 8->8 : oct(0o10)
  - 16->8: oct(oxff)
- 转换16进制：
  - 2->16 : hex(0b111)
  - 8->16: hex(0o10)
  - 16->16: hex(oxff)

### int 类型方法

`bit_length()` 当前数字占用二进制最少位数

bin(18) => 0b10001 => 5 bit

`__abs__()` 绝对值

`abs()` 内部创建数组对象并调用__abs__()数字方法

`__add__(y)` 加号运算, 等于加号`+`

`__divmod__(y)` 返回元祖，分页场景使用

`__float__()` 类型转换

`__floordiv__()` floor 想下取整

`__ge__()` 大于等于

`__le__()` 小于等于

`help(10), help(int)` 帮助函数

### 长整型 long (不可变类型), Python3 不支持

`203020930239`

### 复数 complex

> j表示复数
`(5+4j)`

## 浮点类型 float (不可变类型)

`3.141592`

`sys.float_info`

复数：`3+6e`

## 字符串：str (不可变类型)

### 字符串表示法

- 单引号
- 双引号
- 三引号

### 字符串连接整型必须转换字符串类型

`str(1)+"string"`

- 字符串连接

```py
str=str1+str2
str="===%s==="%(str1+str2)
```

### 路径字符串

`r'C:\now\fishc\ca'`

### 字符串长度

`len(str)`

### 字符串索引

```py
i=str[index]
i=str[-lastIndex]
```

### 字符串切片

``` Python
str=str[0:2]      # strarIndex:endIndx, [:2]
str=str[1:3]      # startIndex:endIndex，不包括endIndex元素`
str=str[2:]       # 第三个元素到最后一个
str=str[-2:]      # 最后两个元素
str=str[1:10:2]   # 2:step
str=str[-1:0:-1]  # 反向取值，不包括第一个0元素值
str=str[-1::-1]   # 反向取值，所有的
str=str[::-1]     # 反向取值，所有的，以步长为顺序决定开始索引和结束索引
```

### 字符串操作

```py
str = "hello world hello hi ho are you"
```

### 查找子串：find, rfind, index, rindex

```py
-1 | index str.find(search [, start=0, end=len(search)])
str.find("llo")      # 2
str.find("good")     # -1
-1 | index  str.rfind("llo")     # 14

error | index str.index(search [, start=0, end=len(search)])
str.index("e")       # 1
str.rindex("llo")    # 14
str.index("good")    # ValueError: substring not found
```

### 查找子串数量：count

`0 | 字符串中子串个数 str.count(search [, start=0, end=len(search)])`
`0 | 字符串中子串个数 str.count("llo")     # 2`

### 替换字符串：replace

`newstr str.replace(old, new [,str.count(old)])`

`newstr str.replace("llo","good")  # hegood world hegood hi ho are you`

对原字符串没有影响

count 替换次数

### 分割字符串：split, 自动识别空白字符

``` Python
str.split(seperator[, count])
str.split(" ")  # ['hello', 'world', 'hello', 'hi', 'ho', 'are', 'you']
str.split(" ",2)# ['hello', 'world', 'hello hi ho are you']
```

### 单词首字母大写：title

> 以特殊字符作为分隔符作为单词边界

`str.title()    # Hello World Hello Hi Ho Are You`

### 串前缀开始、后缀结束：startswith,endswith

``` Python
str.startswith("hello")  # True
str.startswith("ehello") # False
str.endswith("you")      # True
```

- 上传文件

1. 检查后缀名
2. 检查内容

### 单词首字母大写

`str.capitalize()`

### 大小写转换：lower,upper

``` Python
str.lower()    # hello world hello hi ho are you
str.upper()    # HELLO WORLD HELLO HI HO ARE YOU
```

### tab键个数

`'hello\t word'.expandtabs(tabsize=20)`

``` Python
'hello\t world'.expandtabs(20)
'hello\t world'.expandtabs(20)
```

### 对齐：ljust,rjust,center

``` Pytohn
s="hi"
左对齐：str.ljust(5)  # "hi   "
右对齐：str.rjust(5)  # "   hi"
中对齐：str.center(5) # " hi  "

'hello world How are you?'.center(50,'*')
'*************hello world How are you?*************'
```

### 修剪：lstrip,rstrip,strip

``` Python
s=" hi "
左修剪：str.lstrip()
右修剪：str.rstrip()
修剪：str.strip()
```

### 分割三部分：partition,rpartition, 返回元组

``` Python
s="hello world title how title are you"

s.partition("title")    # ('hello world ', 'title', ' how title are you')

s.rpartition("title")   # ('hello world title how ', 'title', ' are you')

s.partition("titles")    # ('hello world title how title are you', '', '')

s.rpartition("titles")   # ('', '', 'hello world title how title are you')
```

### 行切割：splitlines，返回列表

``` Python
s="hello world\n how areyou\nhi"
s.splitlines()          # ['hello world', ' how areyou', 'hi']
```

### 只包含字符则返回 True 否则返回 False：isalpha

``` Python
s="123"
s1="abc 1"
s2="abc"
s.isalpha()    # False
s1.isalpha()   # False
s2.isalpah()   # True
```

### 只包含数字则返回 True 否则返回 False： isdigit

``` Python
s="123"
s1="12 a"
s2="abc"
s.isdigit()`    # True
s1.isdigit()`   # False
s2.isdigit()`   # False
```

### 合并：join

``` Python
s="="
li=["a","b","c"]
s.join(li)`      # a=b=c
```

## 元组 tuple

> 只读列表

### 定义元组

``` Python
t=(3,)      # 注意：单个元素元组最后必须加逗号
t=(11,22)
a,b=t          # a=11,b=22
```

### 访问

`t[index]`

### 修改：不能

### 删除：不能

`t.index(ele)`
`t.count(ele)`

## list 列表 (可变类型)

### 创建列表

``` Python
li = list([1,2,3])
li = [1,2,3]
```

### 添加

``` Python
li.append(ele)            # 压栈，没有返回值[null]，整体添加
li.insert(index,ele)     # 数据类型
li.extend(li2) == li+li2  # 整体分割成元素分别添加
区别：li 变为 li+li2, 而 li+li2 的 li 值不变  
```

### 删除

``` Python
li.pop()         # 弹栈，delete last element
li.remove(ele)   # 删除查找元素的第一个
del li[index]    # 根据下标删除
li.clear()       # 清空 []
```

### 修改

`li[index] = value`

### 切片

`li[start:end]`

### 元素次数

`li.count(ele)`

### 索引位置

`error|int li.index(ele)`

### 查询：in, not in 是否[不]存在

`boolean "元素" [not] in LIST`

### max, min

``` Python
max([1,2,3,4]) # 4
min([1,2,3,4]) # 1
max("abcdefA") # A (ASCII 排序)
ord('A') # 65
ord('a') # 97
ord(' ') # 32
```

### 倒序

`name_list.reverse()`

### 排序

`name_list.sort() # 升序`

ASCII码顺序：数字,特殊字符，字母

`sorted(li)` 函数

### 降序

`name_list.sort(reverse=True)`

### range()

## 字典 dict (可变类型)

### 创建字典

> 存在就覆盖，否则就增加

`di={'k1':'v1','k2':'v2'}`

### 修改字典

`di["k1"]="value"`

### 添加字典

`di["new"]="new value"`

### 删除字典

`error|bool del di["k1"]`

### 删除元素

``` Python
d.pop('key')      # 返回值
d.popitem()       # 删除随机元素
```

### 查询值

``` Python
di["key"]
**di.get("key")**      # 没有找到返回空，None
```

### 元素个数

`len(di)`

### key 列表

> 返回没有索引的键列表

`di.keys()`

### value 列表

> 返回没有索引的值列表

`di.values()`

### items (键，值)元组的列表

> 返回键值对

`di.items()`

`[('k1','v1'),('k2','v2')]`

### 遍历

``` Python
ele in d.keys()
ele in d.values()
k,v in d.items()
```

### 排序元祖

``` Python
info=[{'name':'banzhang','age':10},{'name':'fubanzhang','age':9},{'name':'xiaoming',age':20}]
info.sort(key=lambda x:x['name'])
> x是元素，即字典
> x['name'],字典的name属性
> ASCII码比较
```

### 设置值：键存在，不改动，返回字典中响应的键对应的值

`d.setdefault("age",34)`

### 设置值：键不存在，再字典中增加新的键值对，并返回相应的值

`d.setdefault("age",34)`

### 键值对儿

`dict.fromkeys([A,B,C],D)`

## 强制类型转换

``` python
int(变量)

float(变量)

str(变量)

bool(变量)

list(变量)

tuple(变量)

dic(变量)

set(变量)
```

### 获取变量数据类型

`type(变量)`

## 集合

> 集合元素不能有重复值

集合：可变的数据类型，元素必须是不可变的数据类型，无序，不重复

``` python
s = set([1,2,33,33,2,1,4,11,11,11])
li = list(s)
```

### 查看方法

``` python
# 告诉我列表拥有的所有方法
print(dir([]))

# 列表的所有方法
print(dir({}))

# 字符串的所有方法
print(dir(''))

# 列表拥有的方法
print(dir(range(10)))

# 双下的方法
print([1].__add__([2]))
print([1] + [2])


# 可迭代的对象都有`__iter__`
ret = set(dir([])) & set(dir({})) & set(dir('')) & set(dir(range(10)))
print(ret) # iterable


print('__iter__' in dir(int)) # False
print('__iter__' in dir(bool)) # False
print('__iter__' in dir(list)) # True
print('__iter__' in dir(dict)) # True
print('__iter__' in dir(set)) # True
print('__iter__' in dir(tuple)) # True
print('__iter__' in dir(enumerate([]))) # True
print('__iter__' in dir(range(1))) # True

# 能被for循环的数据类型就一定拥有__iter__方法



# 列表执行了__iter__()之后的返回值就是一个迭代器
print([].__iter__())

```

### Counter

### 有序字典 orderedDict

### 默认字典 defaultDict

### 可命名元祖(namedtuple)

> 创建一个包含tuple 所有功能以及其他功能的类型

### 队列(deque)

> Python 内置的一个线程安全的双向队列

- 单向队列
- 双向队列

## 深浅拷贝

- 对于数字和字符串类型，深浅拷贝都是同一个内存地址

## 可变类型不能作为字典的key

```py
a=[1,2,3]
b={a:"test"}
```

根据key找到对应的value，是因为通过获得的哈希值（哈希表中有对应的内存地址）找到key对应的值。同一个字典中不能相同的key，因为不能有相同的哈希值。