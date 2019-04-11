#-*- coding: utf-8 -*-
class User:
  def __init__(self, pw):
    if len(pw) >= 6:
      self.__password = pw
    else:
      print("密码%s, 长度不符合规范"%pw)

  def __str__(self):
    return '用户名为：%s, 密码为: %s'%(self.username, self.__password)

  def set_password(self, pw):
    if len(pw) >= 6:
      self.__password = pw
    else:
      print("密码%s, 长度不符合规范"%pw)

  def get_password(self):
    return self.__password

u = User("abc")
u.username = 'name'
# u.__password = '123456'
u.set_password("123456789")
# print(u)
print(u.get_password())