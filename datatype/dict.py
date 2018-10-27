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


class dict(object):
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def clear(self): # real signature unknown; restored from __doc__
        """ 清除内容 """
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ 浅拷贝 """
        """ D.copy() -> a shallow copy of D """
        pass

    @staticmethod # known case
    def fromkeys(S, v=None): # real signature unknown; restored from __doc__
        """
        dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
        v defaults to None.
        """
        pass

    def get(self, k, d=None): # real signature unknown; restored from __doc__
        """ 根据key获取值，d是默认值 """
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def has_key(self, k): # real signature unknown; restored from __doc__
        """ 是否有key """
        """ D.has_key(k) -> True if D has a key k, else False """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """ 所有项的列表形式 """
        """ D.items() -> list of D's (key, value) pairs, as 2-tuples """
        return []

    def iteritems(self): # real signature unknown; restored from __doc__
        """ 项可迭代 """
        """ D.iteritems() -> an iterator over the (key, value) items of D """
        pass

    def iterkeys(self): # real signature unknown; restored from __doc__
        """ key可迭代 """
        """ D.iterkeys() -> an iterator over the keys of D """
        pass

    def itervalues(self): # real signature unknown; restored from __doc__
        """ value可迭代 """
        """ D.itervalues() -> an iterator over the values of D """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ 所有的key列表 """
        """ D.keys() -> list of D's keys """
        return []

    def pop(self, k, d=None): # real signature unknown; restored from __doc__
        """ 获取并在字典中移除 """
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

    def popitem(self): # real signature unknown; restored from __doc__
        """ 获取并在字典中移除 """
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        """
        pass

    def setdefault(self, k, d=None): # real signature unknown; restored from __doc__
        """ 如果key不存在，则创建，如果存在，则返回已存在的值且不修改 """
        """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
        pass

    def update(self, E=None, **F): # known special case of dict.update
        """ 更新
            {'name':'alex', 'age': 18000}
            [('name','sbsbsb'),]
        """
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
        If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
        In either case, this is followed by: for k in F: D[k] = F[k]
        """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """ 所有的值 """
        """ D.values() -> list of D's values """
        return []

    def viewitems(self): # real signature unknown; restored from __doc__
        """ 所有项，只是将内容保存至view对象中 """
        """ D.viewitems() -> a set-like object providing a view on D's items """
        pass

    def viewkeys(self): # real signature unknown; restored from __doc__
        """ D.viewkeys() -> a set-like object providing a view on D's keys """
        pass

    def viewvalues(self): # real signature unknown; restored from __doc__
        """ D.viewvalues() -> an object providing a view on D's values """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __contains__(self, k): # real signature unknown; restored from __doc__
        """ D.__contains__(k) -> True if D has a key k, else False """
        return False

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, seq=None, **kwargs): # known special case of dict.__init__
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass

    __hash__ = None