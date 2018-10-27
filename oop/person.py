class Person:                 # 类名
  country = 'China'         # 创造了一个只要是这个类就一定有的属性
                              # 类属性 静态属性
  def __init__(self, *args):  # 初始化方法，self是对象，是一个必须传的参数
    # self就是一个可以存储很多属性的大字典
    self.name = args[0]   # 往字典里添加属性的方式发生了一些变化
    self.hp = args[1]
    self.aggr = args[2]
    self.sex = args[3]

  def walk(self,n):         # 方法，一般情况下必须传self参数，且必须写在第一个
                            # 后面还可以传其他参数，是自由的
    print('%s走走走,走了%s步'%(self.name,n))

# print(Person.country)        # 类名 可以查看类中的属性，不需要实例化就可以查看
alex = Person('狗剩儿',100,1,'不详')  # 类名还可以实例化对象，alex对象   # 实例化
print(alex.__dict__) # 查看所有属性
print(alex.name)  # 查看属性值
print(alex.hp)  # 查看属性值
alex.walk(5)    # Person.walk(alex，5)  # 调用方法 类名.方法名(对象名)
 
print(Person.__dict__['country'])
# Person.__dict__['country'] = '印度' #  __dict__ 对于类中的名字只能看 不能操作
print(alex.__dict__['name'])
alex.__dict__['name'] = '二哥'
print(alex.__dict__)
print(alex.name)
print(alex.name)
alex.name = '二哥'
alex.__dict__['name'] = '二哥' # __dict__ 对于对象的增删改查操作都可以通过字典的语法进行
alex.age = 83
print(alex.__dict__)
print(alex.name)
 
# 对象 = 类名()
# 过程：
    # 类名() 首先 会创造出一个对象，创建了一个self变量
    # 调用init方法，类名括号里的参数会被这里接收
    # 执行init方法
    # 返回self
# 对象能做的事：
    # 查看属性
    # 调用方法
    # __dict__ 对于对象的增删改查操作都可以通过字典的语法进行
# 类名能做的事：
    # 实例化
    # 调用方法 : 只不过要自己传递self参数
    # 调用类中的属性,也就是调用静态属性
    # __dict__ 对于类中的名字只能看 不能操作