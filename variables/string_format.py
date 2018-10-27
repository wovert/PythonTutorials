# __author__ = 'Administrator'
# date = 2018/4/1
# 字符串格式化输出

name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

try:
    number = float(salary)
except ValueError:
    print("not a float datatype")
    exit()

msg = '''
------ info of User -----
Name: %s
Age: %d
Job: %s
Salary: %.2f
rate:3%%
------ end --------
''' % (name, int(age), job, float(salary))

print(msg)

number = 100
print("number变量里的值是%d"%number)
 
names = "东哥"
print("名字是:%s"%names)