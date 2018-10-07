class Dog:
 
    def __init__(self, new_name):
        self.name = new_name
        self.__age = 0#定义了一个私有的属性,属性的名字是__age
 
    def set_age(self,new_age):
        if new_age>0 and new_age<=100:
            self.__age = new_age
        else:
            self.__age = 0
 
    def get_age(self):
        return self.__age
 
dog = Dog("小白")
#dog.age = -10
#dog.name = "小白"
 
#print(dog.age)
 
 
dog.set_age(-10)
age = dog.get_age()
print(age)
 
#dog.get_name()
 
#dog.__age = -10
#print(dog.__age) # AttributeError: 'Dog' object has no attribute '__age'
