from math import pi
class Circle:
  def __init__(self, r):
    self.r = r
  
  @property
  def perimeter(self):
    return 2*pi*self.r

  @property
  def area(self):
    return self.r**2*pi
c = Circle(5)
print(c.area)
print(c.perimeter)

class Person:
  def __init__(self, name, high, weight):
    self.name = name
    self.high = high
    self.weight = weight

  @property
  def bmi(self):
    return self.weight/self.high**2

j = Person('金老板', 1.6, 90)
print(j.bmi)