# 赋值运算
l1 = [1,2,3]
l2 = l1
l1.append('a')
print(l1,l2)
 
#copy
l1 = [1,2,3]
 l2 = l1.copy()
print(l1,l2)
print(id(l1),id(l2))

#l2.append('a')
print(l1,l2)
 
l1 = [1,2,[4,5,6],3]
l2 = l1.copy()
 
print(l1,id(l1))
print(l2,id(l2))
l1.append('a')
print(l1,l2)
l1[2].append('a')
print(l1,l2)
print(id(l1[2]))
print(id(l2[2]))

import copy
l1 = [1,2,[4,5,6],3]
l2 = copy.deepcopy(l1)
print(l1,id(l1))
print(l2,id(l2))
l1[2].append('a')
print(l1,l2)
 
l1 = [1,[1],2,3,4]
l2 = l1[:]
l1[1].append('a')

#l2 的结果是什么?
 
 
print(l1,id(l1))
print(l2,id(l2))
print(l1[1] is l2[1])
 
li = ['alex','taibai','wusir','egon']
for i in li:
  print(li.index(i),i)
 
for index,i in enumerate(li,1):
  print(index,i)