# -*- coding: utf-8 -*-
num = 10
print(id(num)) # 140259427915648
num += 0 # 引用地址的值修改
print(id(num)) # 140259427915648
num = num + 10 # 使用新的内存空间
print(id(num)) # 140259427915408