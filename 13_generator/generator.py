# 自定义函数
# def generator():
#   print(1)
#   return 'a'

# 生成器函数
def generator():
  print(1)
  yield 'a'

# re 是生成器对象
re = generator()

# re是迭代器
# re.__next__()方法返回生成器对象返回结果
print(re.__next__())

def generator2():
  print(1)
  yield 'a'
  print(2)
  yield 'b'

g = generator2()

print(g.__next__()) # 执行之后函数print(2)开始处
print(g.__next__()) # 执行 print(2) yield 'b'
# print(g.__next__()) # 迭代器没有返回值

def wahaha():
  for i in range(2000000):
    yield '哇哈哈%s'%i

g = wahaha()

count = 0
for i in g:
  count += 1
  print(i)
  if count > 50:
    break

print('*********', g.__next__())


# 可迭代对象
l = [1,2,3,4,5]

# 列表l自动转化成可迭代对象。每一次循环都会拿到新的迭代器
for i in l:
  print(i)
  if i == 2:
    break

# 列表l自动转化成可迭代对象
for i in l:
  print(i)


def tail(filename):
  f = open(filename, encoding='utf-8')
  while True:
    line = f.readline()
    if line:
      yield line.strip('\r\n') # 只能删除开头或是结尾的字符，不能删除中间部分的字符
    else:
      break

fg = tail('generator.py')
print('======================================')
print(fg.__next__())
print('======================================')
for i in fg:
  print(i)