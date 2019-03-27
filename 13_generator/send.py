def generator():
  print(123)
  content = yield 1
  print('==========', content)
  print(456)
  yield 2

g = generator()
res = g.__next__()
print('***', res)
res = g.send('hello')
print('***', res)