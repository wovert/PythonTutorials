# 正则表达式

## re 模块

``` py
import re
phone_number = input('please input your phone number ： ')
if re.match('^(13|14|15|18)[0-9]{9}$',phone_number):
  print('是合法的手机号码')
else:
  print('不是合法的手机号码')

print(r'\\n')
print(r'\n')
```

- findall
- search
- match

``` py
ret = re.findall('[a-z]+', 'eva egon yuan')
# 返回所有满足匹配条件的结果,放在列表里
print(ret)

ret = re.search('a', 'eva egon yuan')
if ret:
  print(ret.group())

# 从前往后，找到一个就返回,返回的变量需要调用group才能拿到结果
# 如果没有找到，那么返回None，调用group会报错

ret = re.match('[a-z]+', 'eva egon yuan')
if ret:
  print(ret.group())
# match是从头开始匹配，如果正则规则从头开始可以匹配上，就返回一个变量。
# 匹配的内容需要用group才能显示
# 如果没匹配上，就返回None，调用group会报错

ret = re.split('[ab]', 'abcd')
# 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4',1)

#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')
# 将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')
#将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())
ret = obj.search('abcashgjgsdghkash456eeee3wr2') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果
for i in ret:
  print(i.group())

ret = re.search('^[1-9](\d{14})(\d{2}[0-9x])?$','110105199912122277')
print(ret.group())
print(ret.group(1))
print(ret.group(2))

ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可
ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']

ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']
```