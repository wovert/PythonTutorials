# 面向对象的三大特性 ： 继承 多态 封装
# 组合
# 人狗大战
class Dog:
    def __init__(self,name,aggr,hp,kind):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = kind
 
    def bite(self,person):
        person.hp -= self.aggr
 
class Person:
    def __init__(self,name,aggr,hp,sex):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.sex = sex
        self.money = 0
 
    def attack(self,dog):
        dog.hp -= self.aggr
 
    def get_weapon(self,weapon):
        if self.money >= weapon.price:
            self.money -= weapon.price
            self.weapon = weapon
            self.aggr += weapon.aggr
        else:
            print("余额不足，请先充值")
 
class Weapon:
    def __init__(self,name,aggr,njd,price):
        self.name = name
        self.aggr = aggr
        self.njd = njd
        self.price = price
 
    def hand18(self,person):
        if self.njd > 0:
            person.hp -= self.aggr * 2
            self.njd -= 1
 
alex = Person('alex',0.5,100,'不详')
jin = Dog('金老板',100,500,'teddy')
w = Weapon('打狗棒',100,3,998)
# alex装备打狗棒
alex.money += 1000
alex.get_weapon(w)
print(alex.weapon)
print(alex.aggr)
alex.attack(jin)
print(jin.hp)
alex.weapon.hand18(jin)
print(jin.hp)
 
# 组合 ：一个对象的属性值是另外一个类的对象
#        alex.weapon 是 Weapon类的对象