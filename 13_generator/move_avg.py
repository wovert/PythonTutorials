def init(func): # 装饰器 func = average
  def inner(*args, **kwargs):
    g = func(*args, **kwargs)
    g.__next__()
    return g
  return inner


@init # average=init(average)=inner
def average():
  sum = 0
  count = 0
  avg = 0
  while True:
    num = yield avg
    sum += num
    count += 1
    avg = sum/count

g = average() # inner
# g.__next__()
avg1 = g.send(10)
print(avg1)
avg2 = g.send(20)
print(avg2)