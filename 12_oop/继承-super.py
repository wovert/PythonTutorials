class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
    def eat(self):
        print('吃药回血')
        self.hp+=100
 
class Dog(Animal):
    def __init__(self,name,aggr,hp,kind):
        super().__init__(name,aggr,hp)  # 只在新式类中有，python3中所有类都是新式类
        self.kind = kind       # 派生属性
    def eat(self):print('dog eating')