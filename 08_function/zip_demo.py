x = [1,2,3]
y = [4,5,6]

z = zip(x,y)
print(list(z)) # [(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x,y))
print(x == list(x2) and y == list(y2)) # True