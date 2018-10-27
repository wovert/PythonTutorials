import re

# 从前往后，找一个就返回，返回的变量需要调用group 才能拿到结果
# 如果没有找到，则返回None,调用 grouop 会报错
res = re.search('e', 'eva egon yuan')
if res:
  print(res.group()) # e

r = re.match('e', 'eva egon yuan')
if r:
  print(r.goup())

ret = re.sub('\d', 'H', 'sbdnlabc', 1)
print(ret) # 将数字替换成'H', 参数1标识只替换1个

resp = re.split('[ab]', 'abcd')
print(resp) # ['','','cd]

ren = re.subn('\d', 'H', 'eva2egon4yuan4')
# 将数字替换成'H', 返回元祖(替换的结果，替换了多少次)

# 将正则表达式编译成为一个正则表达式对象，规则要匹配的是3个数字
obj = re.compile('\d{3}')
reo = obj.search('abc123eeee') # 将正则表达式调用 search, 参数为待匹配
print(reo.group()) # 记过123

rd = re.finditer('\d', 'ds3sy47834a') # 返回一个存放匹配结果的迭代器
print(rd) # 
print(next(rd).group()) # 查看第一个结果
print(next(rd).group()) # 查看第二个结果
print([i.group()] for i in rd) # 查看剩余的左右结果
