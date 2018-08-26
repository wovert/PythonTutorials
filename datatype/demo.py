'''
python2 python3

'''
# python2
# print()  print 'abc'
# range()   xrange() 生成器
# raw_input()

# python3
# print('abc')
# range()
# input()

# = 赋值 == 比较值是否相等   is 比较，比较的是内存地址  id(内容)
# li1 = [1,2,3]
# li2 = li1
# li3 = li2
# print(id(li1),id(li2))

# 数字，字符串 小数据池
# 数字的范围 -5 -- 256
# 字符串：1，不能有特殊字符
#        2，s*20 还是同一个地址，s*21以后都是两个地址
# i1 = 6
# i2 = 6
# print(id(i1),id(i2))
# i1 = 300
# i2 = 300
# print(id(i1),id(i2))


# 剩下的 list dict tuple set
# l1 = [1,]
# l2 = [1,]
# print(l1 is l2)

# s = 'alex'
# s1 = b'alex'
# print(s,type(s))
# print(s1,type(s1))

# s = '中国'
# print(s,type(s))
# s1 = b'中国'
# print(s1,type(s1))

s1 = 'alex'
# encode 编码，如何将str --> bytes, ()
s11 = s1.encode('utf-8')
s11 = s1.encode('gbk')
print(s11)
s2 = '中国'
s22 = s2.encode('utf-8')
s22 = s2.encode('gbk')
print(s22)