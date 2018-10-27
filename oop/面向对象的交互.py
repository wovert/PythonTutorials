class Dog:
    def __init__(self,name,blood,aggr,kind):
        self.name = name
        self.hp = blood
        self.aggr = aggr
        self.kind = kind
    def bite(self,person):
        # 狗咬人，人掉血
        person.blood -= self.aggr
 
class Person:
    def __init__(self,name,blood,aggr,sex):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.sex = sex
    def attack(self,dog):
        dog.hp -= self.aggr
        if dog.hp <= 0:
            print('%s打了%s,%s被打死了，扑街~~~'%(self.name,dog.name,dog.name))
        else:
            print('%s打了%s,掉了%s血'%(self.name,dog.name,self.aggr))
 
jin = Dog('金老板',100,20,'teddy')
# print(jin.name)
alex = Person('alex',999,998,'不详')
jin.bite(alex)   # Dog.bite(jin,alex)
print(alex.blood)
# alex attack
alex.attack(jin)  # Person.attack(alex,jin)
print(jin.hp)