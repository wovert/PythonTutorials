a = [11,22,33]
b = [44,55]

#因为a.append(b)已经修改了a的元素...但是a.append(b)并没有一个结果,所以 接下来a=空,因此a为None
a = a.append(b)

print(a)
