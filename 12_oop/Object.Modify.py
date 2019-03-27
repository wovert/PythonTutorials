class Person:
  def __init__(self, name):
    self.__name = name
  
  @property
  def name(self):
    return self.__name + 'sb'

  @name.setter
  def name(self, new_name):
    self.__name = new_name

  @name.deleter
  def name(self):
    print('删除__name属性')
    del self.__name

p = Person('泰格')
print(p.name)
p.name = '全班'
print(p.name)
del p.name # 删除属性
# print(p.name)