#dict
'''
#数据类型划分：可变数据类型，不可变数据类型
不可变数据类型：元组，bool int str       可哈希
可变数据类型：list，dict set             不可哈希
dict key 必须是不可变数据类型，可哈希，
    value：任意数据类型。
dict 优点：二分查找去查询
         存储大量的关系型数据
      特点：无序的
#55
#20
#60
#40
#50
#55
'''
# dic = {
#     'name':['大猛','小孟'],
#     'py9':[{'num':71,'avg_age':18,},
#            {'num': 71, 'avg_age': 18, },
#            {'num': 71, 'avg_age': 18, },
#            ],
#     True:1,
#     (1,2,3):'wuyiyi',
#     2:'二哥',
# }
# print(dic)
dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}
#增：
# dic1['high'] = 185  #没有键值对，添加
# dic1['age'] = 16  #如果有键，则值覆盖
 
# dic1.setdefault('weight')  # 有键值对，不做任何改变，没有才添加。
# dic1.setdefault('weight',150)
# dic1.setdefault('name','二哥')
# print(dic1)
 
#删
# print(dic1.pop('age'))   # 有返回值，按键去删除
# print(dic1.pop('二哥',None))   # 可设置返回值
# print(dic1)
 
# print(dic1.popitem())  # 随机删除 有返回值 元组里面是删除的键值。
# # print(dic1)
 
# del dic1['name1']
# print(dic1)
# del dic1
# print(dic1)
 
# dic1.clear() #清空字典
 
#改  update
# dic1['age'] = 16
 
# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)  #
#
# print(dic)
# print(dic2)
dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}
#查
# print(dic1.keys(),type(dic1.keys()))
# print(dic1.values())
# print(dic1.items())
 
# for i in dic1:
#     print(i)
# for i in dic1.keys():
#     print(i)
 
# for i in dic1.values():
#     print(i)
 
# a,b = 1,2
# print(a,b)
 
# a = 1
# b = 2
# a,b = b,a
# print(a,b)
# a,b = [1,2],[2,3]
# a,b = (1,2)
# print(a,b)
 
# for k,v in dic1.items():
#     print(k,v)
 
# v1 = dic1['name']
# print(v1)
 
# v2 = dic1['name1']  # 报错
# print(v2)
 
# print(dic1.get('name1','没有这个键'))