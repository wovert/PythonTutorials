# java ： 面向对象编程
# 设计模式   —— 接口
# 接口类 ： python原生不支持
# 抽象类 ： python原生支持的
from abc import abstractmethod,ABCMeta
class Payment(metaclass=ABCMeta):  # 元类 默认的元类 type
    @abstractmethod # 声明抽象类方法
    def pay(self,money):pass   # 没有实现这个方法

# 规范 ：接口类或者抽象类都可以
# 接口类 支持多继承，接口类中的所有的方法都必须不能实现 —— java
# 抽象类 不支持多继承，抽象类中方法可以有一些代码的实现 —— java
class Wechat(Payment):
    def pay(self,money):
        print('已经用微信支付了%s元'%money)
 
class Alipay(Payment):
    def pay(self,money):
        print('已经用支付宝支付了%s元' % money)
 
class Applepay(Payment):
    def pay(self,money):
        print('已经用applepay支付了%s元' % money)
 
def pay(pay_obj,money):  # 统一支付入口
    pay_obj.pay(money)
 
# wechat = Wechat()
# ali = Alipay()
app = Applepay()
# wechat.pay(100)
# ali.pay(200)
p = Payment()