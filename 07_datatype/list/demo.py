import random

list = ["PHP", "NodeJS", "Go", "Python", "Rust", "C++"]

# get
print(list[0]) # PHP
print(list[1:3]) # ['NodeJs', 'Go']
print(list[2:]) # 到最后：['Go', 'Python', 'Rust', 'C++']
print(list[2:-1]) # -1:倒数第二个 ['Go', 'Python', 'Rust']
print(list[0:-1:2]) # 从开始到倒数第二个，步长2 ['PHP', 'Go', 'Rust']
print(list[4::-2]) # 从第5个元素开始到结束，步长2 ['Rust', 'Go', 'PHP']

# append/insert
list.append("Ruby")
print(list)
list.insert(1, "Java")
print(list)

# remove/pop/del
list.remove('PHP') # delete 'PHP' element
print(list)
list.pop() # delete last element
print(list)
del list[0] # delelte first element
print(list)

# count: 计算元素出现次数
print(list.count('Go'))

# extend: 扩展
a = [1,3,5]
b = [2,4,6]
a.extend(b)
print(a)
print(b)

# index: 元素索引位置
print(list.index("Go"))

# reverse
print(list)
list.reverse()
print(list)

# sort
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# in
print("Go" in list)

# random

random_list = []
# for i in range(10):
#     ran = random.randint(1, 50)
#     if ran not in random_list:
#         random_list.append(ran)

count = 0
while count < 10:
    ran = random.randint(1, 50)
    if ran not in random_list:
        random_list.append(ran)
        count += 1
print(random_list)
print(max(random_list))
print(min(random_list))
print(sorted(random_list))
print(sorted(random_list, reverse=True))