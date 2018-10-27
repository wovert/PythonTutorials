import copy

# 字符串、数字

a1 = "123123"
a2 = a1

# 变量的内存地址
print('a1:',id(a1))
print('a2:',id(a2))


# 浅拷贝
a3 = copy.copy(a1)
print('a3:',id(a3))

# 深拷贝
a4 = copy.deepcopy(a1)
print('a4:',id(a4))

print("-"*30)

# 元祖/列表/字典
n1 = {"k1":"wu","k2":123, "k3": ["alex",678]}
n2 = n1
n3 = copy.copy(n1)
n4 = copy.deepcopy(n1)

print('n1:',id(n1), ',n1.k3:', id(n1['k3']), ',n1.k3[0]:',id(n1['k3'][0]))
print('n2:',id(n2), ',n2.k3:', id(n2['k3']), ',n2.k3[0]:',id(n2['k3'][0]))
print('n3:',id(n3), ',n3.k3:', id(n3['k3']), ',n3.k3[0]:',id(n3['k3'][0]))
print('n4:',id(n4), ',n4.k3:', id(n4['k3']), ',n4.k3[0]:',id(n4['k3'][0]))