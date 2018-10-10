import collections

obj = collections.Counter('sbdnllichengguo')
print(obj) 
'''Counter({'n': 2, 'l': 2, 'g': 2, 's': 1, 'b': 1, 'd': 1, 'i': 1,'c': 1, 'h': 1, 'e': 1, 'u': 1, 'o': 1})'''

res = obj.most_common(4) # 排序后的前四位
print(res) # [('n', 2), ('l', 2), ('g', 2), ('s', 1)]

# 获取元素个数
for k in obj.elements():
  print(k)

# 获取元素个数
for k,v in obj.items():
  print(k,v)
