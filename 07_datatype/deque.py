import collections
import queue

# 创建双向队列
d = collections.deque()
d.append('1')
d.append('10')
d.append('1')
print(d)
print(d.count('1')) # 2

d.extend(['yy','uu','ii']) # 向右扩展
print(d)

d.extendleft(['aa','bb','cc']) # 向左扩展
print(d)

d.rotate(1) # 最后元素放到第一个元素上
print(d)

'''
单项队列
'''

# 创建单项队列
sq = queue.Queue()
sq.put('123')
sq.put('456')
print(sq.qsize()) # 2
print(sq.get()) # 123
