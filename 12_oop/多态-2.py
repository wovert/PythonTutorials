# 多态 python 天生支持多态
# def func(int num,str name):
#     pass
#
# func('alex',2)
# class Payment:pass
 
# class Alipay():
#     def pay(self,money):
#         print('已经用支付宝支付了%s元' % money)
#
# class Applepay():
#     def pay(self,money):
#         print('已经用applepay支付了%s元' % money)
#
# def pay(pay_obj,money):  # 统一支付入口  归一化设计
#     pay_obj.pay(money)
#
# pay()
 
# 什么是多态
# python 动态强类型的语言
# 鸭子类型
# list tuple
# 不崇尚根据继承所得来的相似
# 我只是自己实现我自己的代码就可以了。
# 如果两个类刚好相似，并不产生父类的子类的兄弟关系，而是鸭子类型
# list tuple 这种相似，是自己写代码的时候约束的，而不是通过父类约束的
# 优点 ： 松耦合 每个相似的类之间都没有影响
# 缺点 ： 太随意了,只能靠自觉
 
# class List():
#     def __len__(self):pass
# class Tuple():
#     def __len__(self):pass
#
# def len(obj):
#     return obj.__len__()
#
# l = Tuple()
# len(l)
#
# # 强类型语言     多态
# # python 语言    鸭子类型
 
 
# 接口类和抽象类 在python当中的应用点并不是非常必要