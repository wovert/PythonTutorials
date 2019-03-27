class Dog(object):
 
    __instance = None
    __init_flag = False
 
    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建的对象的引用
            return cls.__instance
 
    def __init__(self, name):
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True
 
 
a = Dog("旺财")
print(id(a))
print(a.name)
 
b = Dog("哮天犬")
print(id(b))
print(b.name)