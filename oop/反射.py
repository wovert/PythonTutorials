#反射 *****
# name = 'alex'
# 'name'
 
class Teacher:
    dic = {'查看学生信息':'show_student','查看讲师信息':'show_teacher'}
    def show_student(self):
        print('show_student')
 
    def show_teacher(self):
        print('show_teacher')
 
    @classmethod
    def func(cls):
        print('hahaha')

alex = Teacher()
for k in Teacher.dic:
    print(k)

key = input('输入需求 ：')
# print(Teacher.dic[key])
if hasattr(alex, Teacher.dic[key]):
    func = getattr(alex,Teacher.dic[key])
    func()
# # alex.show_student()  'show_student'
# func = getattr(alex,'show_student')
# func()
 
# hasattr getattr delattr
# if hasattr(Teacher,'dic'):
#     ret = getattr(Teacher,'dic')   # Teacher.dic   # 类也是对象
# # ret2 = getattr(Teacher,'func')         # 类.方法  teacher.func
# # ret2()
#     print(ret)
 
 
# menu = Teacher.dic
# for k in menu:
#     print(k)
 
# 通过反射
# 对象名 获取对象属性 和 普通方法
# 类名 获取静态属性 和类方法 和 静态方法
 
# 普通方法 self
# 静态方法 @staticmethod
# 类方法 @classmethod
# 属性方法 @property
 
# 继承
# 封装的
 
 
# 学员管理系统 ： 开发规范
# 整理面向对象的所有知识点
# 时间计划表 ：周末干什么 中等偏下的 每周来一天自习