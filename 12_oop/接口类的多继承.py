# tiger 走路 游泳
# swan 走路 游泳 飞
# oldying 走路 飞
from abc import abstractmethod,ABCMeta
class Swim_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):pass
 
class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):pass
 
class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):pass
 
class Tiger(Walk_Animal,Swim_Animal):
    def walk(self):
        pass
    def swim(self):
        pass
class OldYing(Fly_Animal,Walk_Animal):pass
class Swan(Swim_Animal,Walk_Animal,Fly_Animal):pass
 
# 接口类  刚好满足接口隔离原则 面向对象开发的思想 规范