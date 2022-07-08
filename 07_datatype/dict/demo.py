'''
- 数据类型划分：可变数据类型，不可变数据类型
  - 不可变数据类型：元组，bool int str       可哈希
  - 可变数据类型：list，dict set            不可哈希
- key 必须是不可变数据类型，可哈希
- value：任意数据类型。

- dict 优点：二分查找去查询, 存储大量的关系型数据
- 特点：无序的
'''
dic = {
  'name':['大猛','小孟'],
  'py9':[
    {'num':71,'avg_age':18,},
    {'num': 71, 'avg_age': 18, },
    {'num': 71, 'avg_age': 18, },
  ],
  True:1,
  (1,2,3):'wuyiyi',
  2:'二哥',
}
print(dic)
person = {'age': 18, 'name': 'jin', 'sex': 'male',}

# append
print("----------append----------")
# person['high'] = 185  #没有键值对，添加
# person['age'] = 16  #如果有键，则值覆盖
 
# person.setdefault('weight')  # 有键值对，不做任何改变，没有才添加
person.setdefault('weight',150)
person.setdefault('name','二哥')
print(person)
 
# remove
print("----------remove----------")
print(person.pop('age'))   # 有返回值，按键去删除
print(person.pop('name', None))   # 可设置返回值
print(person)
 
print(person.popitem())  # 随机删除 有返回值 元组里面是删除的键值。
print(person)
 
# del person['sex']
# print(person)
# del person
print(person)
 
person.clear() #清空字典
print(person)

#update
print("----------update----------")
person['age'] = 16
dic = {"name":"jin","age":18,"sex":"male"}
dic2 = {"name":"alex","weight":75}
dic2.update(dic)

print(dic)
print(dic2)
dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}


#get
print("----------get----------")
print(dic1.keys(), type(dic1.keys()))
print(dic1.values())
print(dic1.items())

print("--------for dic1--------") 
for i in dic1:
    print(i)
print("--------for dic1.keys()--------")
for i in dic1.keys():
    print(i)
print("--------for dic1.values()--------")
for i in dic1.values():
    print(i)

a,b = 1,2
print(a,b)
 
a = 1
b = 2
a,b = b,a
print(a,b)
a,b = [1,2],[2,3]
a,b = (1,2)
print(a,b)
 
print("-------dic1.items()--------")
for k,v in dic1.items():
    print(k,v)
 
v1 = dic1['name']
print(v1)
 
# v2 = dic1['name1']  # 报错
# print(v2)
 
print(dic1.get('name1','没有这个键'))