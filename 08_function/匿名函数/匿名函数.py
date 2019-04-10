stu = [{"name": "zs", "age": 23}, {"name":"laowang", "age": 33}, {"name": "wovert", "age":32}]
a = [22, 33, 93, 19, 38, 72, 93, 10]
a.sort(reverse=True)
print(a)
a.reverse()
print(a)

stu.sort(key=lambda x:x["name"])
print(stu)