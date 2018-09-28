# 林海峰
# egon
# egg_list=['鸡蛋%s'%i for i in range(10)]    #列表推导式
# print(egg_list)
 
# egg_list = []
# for i in range(10):
#     egg_list.append('鸡蛋%s'%i)
# print(egg_list)
 
# print([i*i for i in range(10)])
 
#生成器表达式
# g = (i for i in range(10))
# print(g)
# for i in  g:
#     print(i)
 
# 括号不一样
# 返回的值不一样 === 几乎不占用内存
 
# 老母鸡=('鸡蛋%s'%i for i in range(10))   #生成器表达式
# print(老母鸡)
# for 蛋 in 老母鸡:
#     print(蛋)
 
# g = (i*i for i in range(10))
# g.__next__()