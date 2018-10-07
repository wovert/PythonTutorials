class Cat:
  # 属性

  # 初始化对象
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "[__str__]%s的年龄是：%d"%(self.name, self.age)

  # 方法
  def eat(self):
    print("猫在吃鱼...")
  
  def drink(self):
    print("猫正在喝可乐...")

  def introduce(self):
    # print("%s的年龄是：%d"%(tom.name, tom.age))
    print("%s的年龄是：%d"%(self.name, self.age))

# 创建一个对象
tom = Cat("汤姆", 40)

# 调用对象方法
tom.eat()

# 调用对象方法
tom.drink()

# 给tom指向的对象添加2个属性
tom.name = "汤姆"
tom.age = 40

# 获取属性的第1中方式
print("%s的年龄是:%d"%(tom.name, tom.age))

tom.introduce()

jim = Cat("蓝猫", 20)
jim.name = "蓝猫"
jim.age = 20
jim.introduce()

print(tom)
print(jim)