tuple = ("PHP", "NodeJS", "Go", "Python", "Rust", "C++")

# get
print(tuple[0]) # PHP
print(tuple[1:3]) # ['NodeJs', 'Go']
print(tuple[2:]) # 到最后：['Go', 'Python', 'Rust', 'C++']
print(tuple[2:-1]) # -1:倒数第二个 ['Go', 'Python', 'Rust']
print(tuple[0:-1:2]) # 从开始到倒数第二个，步长2 ['PHP', 'Go', 'Rust']
print(tuple[4::-2]) # 从第5个元素开始到结束，步长2 ['Rust', 'Go', 'PHP']

# count: 计算元素出现次数
print(tuple.count('Go'))

# index: 元素索引位置
print(tuple.index("Go"))

# in
print("Go" in tuple)