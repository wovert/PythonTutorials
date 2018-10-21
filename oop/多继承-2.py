# coding:utf-8
# class F:
#     def func(self): print('F')
# class A(F):pass
#     # def func(self): print('A')
# class B(A):
#     pass
#     # def func(self): print('B')
# class E(F):pass
#     # def func(self): print('E')
# class C(E):
#     pass
#     # def func(self): print('C')
#
# class D(B,C):
#     pass
#     # def func(self):print('D')
#
# d = D()
# # d.func()
# print(D.mro())
 
# 新式类中的继承顺序 ： 广度优先
 
 
class A(object):
    def func(self): print('A')
 
class B(A):
    def func(self):
        super().func()
        print('B')
 
class C(A):
    def func(self):
        super().func()
        print('C')
 
class D(B,C):
    def func(self):
        super().func()
        print('D')
 
b = D()
b.func()
print(B.mro())
#2.7
# 新式类 继承object类的才是新式类 广度优先
# 经典类 如果你直接创建一个类在2.7中就是经典类 深度优先
# print(D.mro())
# D.mro()
 
# 单继承 ： 子类有的用子类 子类没有用父类
# 多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么？
# 经典类中 深度优先
# 新式类中 广度优先
# python2.7 新式类和经典类共存，新式类要继承object
# python3   只有新式类，默认继承object
# 经典类和新式类还有一个区别  mro方法只在新式类中存在
# super 只在python3中存在
# super的本质 ：不是单纯找父类 而是根据调用者的节点位置的广度优先顺序来的
 
# 继续写作业 ：