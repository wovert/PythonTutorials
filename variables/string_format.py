# __author__ = 'Administrator'
# date = 2018/4/1
# 字符串格式化输出

name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

msg = '''
------ info of User -----
Name: %s
Age: %i
Job: %s
Salary: %.2f
------ end --------
''' % (name, int(age), job, float(salary))

print(msg)
