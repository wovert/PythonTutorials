# 圆形类
# 圆环类
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r**2 * pi
    def perimeter(self):
        return 2*pi*self.r
 
class Ring:
    def __init__(self,outside_r,inside_r):
        self.outside_c = Circle(outside_r)
        self.inside_c = Circle(inside_r)
    def area(self):
        return self.outside_c.area() - self.inside_c.area()
    def perimeter(self):
        return self.outside_c.perimeter()+self.inside_c.perimeter()
 
# ring = Ring(20,10)
# print(ring.area())
# print(ring.perimeter())
 
# 创建一个老师类
# 老师有生日
# 生日也可以是一个类
# 组合
class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
 
class Course:
    def __init__(self,course_name,period,price):
        self.name = course_name
        self.period = period
        self.price = price
 
class Teacher:
    def __init__(self,name,age,sex,birthday):
        self.name = name
        self.age = age
        self.sex = sex
        self.birthday =birthday
        self.course = Course('python','6 month',2000)
 
b = Birthday(2018,1,16)
egg = Teacher('egon',0,'女',b)
print(egg.name)
print(egg.birthday.year)
print(egg.birthday.month)
print(egg.course.price)