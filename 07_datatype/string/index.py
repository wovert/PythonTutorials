str = "Hello world hi how are you"
print(str.index("world")) # 6
print(str.rindex("are")) # 19
# print(str.index("ok")) # ValueError: substring not found

name = input("请输入")
nick = input("请输入")

print(name == nick) # 比较内容
print(name is nick) # 比较地址

age = 20
name = "wovert"
# format
message = 'My name is {}, my old is {}'.format(name, age)
print(message)
# in
print("Hello" in str)

# r 保留原格式
print('%s 说：\n哈哈哈\n' %(str))
print(r'%s 说：\n哈哈哈\n')

# find/rfind
str = "Hello world hi how are you"
print(str.find("world")) # 6
print(str.rfind("ok")) # -1