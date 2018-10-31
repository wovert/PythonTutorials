# method 方法
# staticmathod  静态的方法 ***
# classmethod   类方法    ****
# 类的操作行为
# class Goods:
#     __discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * Goods.__discount
#     @classmethod   # 把一个方法 变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
#     def change_discount(cls,new_discount):  # 修改折扣
#         cls.__discount = new_discount
# apple = Goods('苹果',5)
# print(apple.price)
# Goods.change_discount(0.5)   # Goods.change_discount(Goods)
# print(apple.price)
# 当这个方法的操作只涉及静态属性的时候 就应该使用classmethod来装饰这个方法
 
# java
class Login:
    def __init__(self,name,password):
        self.name = name
        self.pwd = password
    
    def login(self):pass
 
    @staticmethod
    def get_usr_pwd():   # 静态方法
        usr = input('用户名 ：')
        pwd = input('密码 ：')
        Login(usr,pwd)
 
Login.get_usr_pwd()
# 在完全面向对象的程序中，
# 如果一个函数 既和对象没有关系 也和类没有关系 那么就用staticmethod将这个函数变成一个静态方法
 
 
 
# 类方法和静态方法 都是类调用的
# 对象可以调用类方法和静态方法么？   可以   一般情况下 推荐用类名调用
# 类方法 有一个默认参数 cls 代表这个类  cls
# 静态方法 没有默认的参数 就象函数一样
 
 
# 面向对象的进阶
# 网络编程