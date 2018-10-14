def generator():
  a = 'abcde'
  b = '12345'
  yield from a
  yield from b

g = generator()
for i in g:
  print(i)