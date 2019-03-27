'abdsafaslhiewhldvjlmvlvk['
# 序列化 —— 转向一个字符串数据类型
# 序列 —— 字符串
 
 
"{'k':'v'}"
 
# 数据存储
# 网络上传输的时候
 
# 从数据类型 --> 字符串的过程 序列化
# 从字符串 --> 数据类型的过程 反序列化
 
# json *****
# pickle ****
# shelve ***
 
# json  # 数字 字符串 列表 字典 元组
    # 通用的序列化格式
    # 只有很少的一部分数据类型能够通过json转化成字符串
# pickle
    # 所有的python中的数据类型都可以转化成字符串形式
    # pickle序列化的内容只有python能理解
    # 且部分反序列化依赖python代码
# shelve
    # 序列化句柄
    # 使用句柄直接操作，非常方便
 
 
# json dumps序列化方法 loads反序列化方法
# dic = {1:"a",2:'b'}
# print(type(dic),dic)
# import json
# str_d = json.dumps(dic)   # 序列化
# print(type(str_d),str_d)
# # '{"kkk":"v"}'
# dic_d = json.loads(str_d) # 反序列化
# print(type(dic_d),dic_d)
 
import json
# json dump load
# dic = {1:"a",2:'b'}
# f = open('fff','w',encoding='utf-8')
# json.dump(dic,f)
# f.close()
# f = open('fff')
# res = json.load(f)
# f.close()
# print(type(res),res)
 
import json
# json dump load
# dic = {1:"中国",2:'b'}
# f = open('fff','w',encoding='utf-8')
# json.dump(dic,f,ensure_ascii=False)
# json.dump(dic,f,ensure_ascii=False)
# f.close()
# f = open('fff',encoding='utf-8')
# res1 = json.load(f)
# res2 = json.load(f)
# f.close()
# print(type(res1),res1)
# print(type(res2),res2)
 
# json
# dumps {} -- > '{}\n'
# 一行一行的读
# '{}\n'
# '{}' loads
# l = [{'k':'111'},{'k2':'111'},{'k3':'111'}]
# f = open('file','w')
# import json
# for dic in l:
#     str_dic = json.dumps(dic)
#     f.write(str_dic+'\n')
# f.close()
 
# f = open('file')
# import json
# l = []
# for line in f:
#     dic = json.loads(line.strip())
#     l.append(dic)
# f.close()
# print(l)
 
import pickle
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = pickle.dumps(dic)
# print(str_dic)  #一串二进制内容
#
# dic2 = pickle.loads(str_dic)
# print(dic2)    #字典
 
# import time
# struct_time1  = time.localtime(1000000000)
# struct_time2  = time.localtime(2000000000)
# f = open('pickle_file','wb')
# pickle.dump(struct_time1,f)
# pickle.dump(struct_time2,f)
# f.close()
# f = open('pickle_file','rb')
# struct_time1 = pickle.load(f)
# struct_time2 = pickle.load(f)
# print(struct_time1.tm_year)
# print(struct_time2.tm_year)
# f.close()
 
# import shelve
# f = shelve.open('shelve_file')
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
# f.close()
#
# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)
 
# import shelve
# f = shelve.open('shelve_file', flag='r')
# existing = f['key']
# print(existing)
#
# f.close()
#
# f = shelve.open('shelve_file', flag='r')
# existing2 = f['key']
# f.close()
# print(existing2)
 
import shelve
# f1 = shelve.open('shelve_file')
# print(f1['key'])
# f1['key']['new_value'] = 'this was not here before'
# f1.close()
 
f2 = shelve.open('shelve_file', writeback=True)
print(f2['key'])
# f2['key']['new_value'] = 'this was not here before'
f2.close()