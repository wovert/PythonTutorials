# class 类名(父类1，父类2):
#     静态属性 = ''          # 静态属性 类属性
#     def __init__(self):    # 初始化方法
#         self.name = 'alex'
#
#     def func(self):        # 动态属性 方法
#         print(self.age)
# 对象 = 类名()
# 对象.方法名()
# 对象.属性名
# 对象.name
# 对象.age = 18
# 对象.func()    #类名.func(对象)
# 组合 ：表达的是 什么有什么的关系       #*****
    # 一个类的属性 是另外一个类的对象
# class Teacher:
#     pass
# class Course:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
# python = Course('python',19800,'6 months')
# class Classes:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course
#         # self.course_name = 'python'
# pys9 = Classes('python_s9',python)
# print(pys9.course.name)
# python.name = 'python全栈'
# print(pys9.course.name)
 
# 命名空间 ： 类和对象分别存在不同的命名空间中
 
# 面向对象的三大特性 ： 继承 多态 封装
# 继承 ：
    # 单继承 ：  ****
        # 父类（超类、基类）
        # 子类（派生类）：派生方法和派生属性
        # 子类的对象在调用方法和属性 ： 先用自己的 自己没有 才用父类的
    # 多继承 ：（面试）
        # 不会超过三个父类，不要超过三层  ***
        # 如果子类自己有用自己的，如果没有就用离子类最近的那个父类的方法
        # 抽象类和接口类   **
        # 经典类和新式类 继承规则不同 深度优先和广度优先  ***** （面试）
    # super 只能在python3中使用   mro   ****
        #super是根据mro广度优先顺序找上一个类
# 多态 ： （面试）
    # 多态和鸭子类型
# 封装 :   *** (面试)
    # 私有的
    # __名字
    # 只能在类的内部调用 子类都无法继承
# 三个装饰器
    # @property         ****   规范 面试   #@name.setter
    # @staticmethod     ***
    # @classmethod      *****  当一个方法只使用了类的静态变量时 就给这个方法加上@classmethod装饰器，默认传cls参数
 
# class Goods:
#     __discount = 0.8
#     @classmethod
#     def change_discount(cls):
#         cls.__discount = 0.5
# Goods.change_discount()