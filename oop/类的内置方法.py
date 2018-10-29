# 内置的类方法 和 内置的函数之间有着千丝万缕的联系
# 双下方法
# obj.__str__  str(obj)
# obj.__repr__ repr(obj)
# class Teacher:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def __str__(self):
#         return "Teacher's object :%s"%self.name
#     def __repr__(self):
#         return str(self.__dict__)
#     def func(self):
#         return 'wahaha'
# nezha = Teacher('哪吒',250)
# print(nezha)  # 打印一个对象的时候，就是调用a.__str__
# print(repr(nezha))
# print('>>> %r'%nezha)
#a.__str__ --> object
# object  里有一个__str__，一旦被调用，就返回调用这个方法的对象的内存地址
# l = [1,2,3,4,5]   # 实例化 实例化了一个列表类的对象
# print(l)
# %s str()  直接打印 实际上都是走的__str__
# %r repr()  实际上都是走的__repr__
# repr 是str的备胎，但str不能做repr的备胎
 
# print(obj)/'%s'%obj/str(obj)的时候，实际上是内部调用了obj.__str__方法，如果str方法有，那么他返回的必定是一个字符串
# 如果没有__str__方法，会先找本类中的__repr__方法，再没有再找父类中的__str__。
# repr(),只会找__repr__,如果没有找父类的
 
# 内置的方法有很多
# 不一定全都在object中
# class Classes:
#     def __init__(self,name):
#         self.name = name
#         self.student = []
#     def __len__(self):
#         return len(self.student)
#     def __str__(self):
#         return 'classes'
# py_s9= Classes('python全栈9期')
# py_s9.student.append('二哥')
# py_s9.student.append('泰哥')
# print(len(py_s9))
# print(py_s9)
 
#__del__
# class A:
#     def __del__(self):   # 析构函数: 在删除一个对象之前进行一些收尾工作
#         self.f.close()
# a = A()
# a.f = open()   # 打开文件 第一 在操作系统中打开了一个文件 拿到了文件操作符存在了内存中
# del a          # a.f 拿到了文件操作符消失在了内存中
# del a   # del 既执行了这个方法，又删除了变量
# 引用计数
 
 
# __call__
class A:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        '''
        打印这个对象中的所有属性
        :return:
        '''
        for k in self.__dict__:
            print(k,self.__dict__[k])
a = A('alex')()