#一切皆文件
import abc #利用abc模块实现抽象类
 
class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        with open('filaname') as f:
            pass
 
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass
 
class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')
    def write(self):
        print('文本数据的读取方法')
 
class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')
 
    def write(self):
        print('硬盘数据的读取方法')
 
class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')
 
    def write(self):
        print('进程数据的读取方法')
 
wenbenwenjian=Txt()
 
yingpanwenjian=Sata()
 
jinchengwenjian=Process()
 
#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()
 
print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)
 
 
# 抽象类 ： 规范
# 一般情况下 单继承 能实现的功能都是一样的，所以在父类中可以有一些简单的基础实现
# 多继承的情况 由于功能比较复杂，所以不容易抽象出相同的功能的具体实现写在父类中
 
 
# 抽象类还是接口类 ： 面向对象的开发规范 所有的接口类和抽象类都不能实例化
# java ：
# java里的所有类的继承都是单继承,所以抽象类完美的解决了单继承需求中的规范问题
# 但对于多继承的需求，由于java本身语法的不支持，所以创建了接口Interface这个概念来解决多继承的规范问题
 
# python
# python中没有接口类  ：
  #  python中自带多继承 所以我们直接用class来实现了接口类
# python中支持抽象类  ： 一般情况下 单继承  不能实例化
  #  且可以实现python代码