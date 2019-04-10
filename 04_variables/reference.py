# -*- coding: utf-8 -*-
num = 10
num += 10 # 引用地址的值修改
print(id(num)) # 47342480
num = num + 10 # 使用新的内存空间
print(id(num)) # 47342240