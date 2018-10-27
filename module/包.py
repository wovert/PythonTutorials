# 把解决一类问题的模块放在同一个文件夹里 —— 包
# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close() ,l)
 
# import glance.api.policy as policy
# policy.get()
#
# from dir.glance.api import policy
# policy.get()
 
# import sys
# sys.path.insert(0,'C:\\Users\\Administrator\\PycharmProjects\\s9\\day21\\dir')
# # print(sys.path)
# from glance.api import policy
# policy.get()
 
# from dir import glance
# glance.db.models.register_models('mysql')
# glance.api.policy.get()
 
# 使用绝对路径 不管在包内部还是外部 导入了就能用
# 不能挪动，但是直观
 
# from dir import glance
# glance.api.policy.get()
# 相对路径
# 可以随意移动包 只要能找到包的位置，就可以使用包里的模块
# 包里的模块如果想使用其它模块的内容只能使用相对路径，使用了相对路径就不能在包内直接执行了