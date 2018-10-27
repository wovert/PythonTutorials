import collections

# 创建类，等同于 defaultdict
MytupleClass = collections.namedtuple('MytupleClass', ['x','y','z'])
obj = MytupleClass(11,22,33)
print(obj.x) # 11
print(obj.y) # 22
print(obj.z) # 33

help(obj) # namedtuple 所有方法

