import time
# time.sleep(100)
# print(time.time())
 
# 格式化时间  —— 字符串： 给人看的
# 时间戳时间 —— float时间 ： 计算机看的
# 结构化时间 —— 元祖 ：计算用的
 
 
# print(time.strftime("%Y-%m-%d %a %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%Y/%m/%d %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%m-%d %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%H:%M"))  #year month day HOUR MINUTE SECOND
 
 
# struct_time = time.localtime()
# print(struct_time)
# print(struct_time.tm_year)
 
import time
# 时间戳和结构化时间
# t = time.time()
# print(t)
# print(time.localtime(3000000000))
# print(time.gmtime(t))
 
# print(time.mktime(time.localtime()))
 
# print(time.strptime('2000-12.31','%Y-%m.%d'))
# print(time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(3000000000)))
 
# print(time.asctime())