set1 = set({1,2,3})
set2 = {1,2,3,[2,3],{'name':'alex'}}  # 错的
print(set1)
print(set2)
set1 = {'alex','wusir','ritian','egon','barry',}

#增
#add
set1.add('女神')
print(set1)

#update
set1.update('abc')
print(set1)

#删除
 
set1.pop()  # 随机删除
print(set1.pop())  # 有返回值
print(set1)
 
set1.remove('alex')  # 按元素
print(set1)
 
#{} set()
set1.clear()
print(set1)  # set()
 
del set1
print(set1)
 
#查
for i in set1:
  print(i)
 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1 & set2
print(set3)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}
 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7,8}
print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7}
 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 - set2)  # {1, 2, 3}

#set1独有的
print(set1.difference(set2))  # {1, 2, 3}
 
set1 = {1,2,3,}
set2 = {1,2,3,4,5,6}

print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。
 
print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。
 
 
#去重
li = [1,2,33,33,2,1,4,5,6,6]
set1 = set(li)
# print(set1)
li = list(set1)
print(li)
s1 = {1,2,3}
print(s1,type(s1))
 
s = frozenset('barry')
print(s,type(s))
for i in s:
  print(i)

```