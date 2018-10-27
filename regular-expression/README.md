# 正则表达式

- 前面的 `*.+.?` 等都是贪婪匹配，也就是说尽可能的匹配，后面加`?`好时其变成惰性匹配

- 惰性匹配：`<.*?>`

- 非贪婪匹配
  - `*?`重复任意次；但尽可能少重复
  - `+?` 重复一次或更多次，但尽可能少重复
  - `??` 重复0次或1次，但尽可能少重复
  - `{n,m}?` 重复n到m次，但尽可能少重复
  - `{n,}?` 重复n次以上，但仅可能少重复

- `.*?`用法
  - `.` 任意字符
  - `*` 是取 0 至 无限长度
  - `?` 是非贪婪模式
  - 何时一起就是，取尽量少的任意字符，一般不会这么单独写，他大多用在； `.*?x`, 就是取前面任意长度的字符，直到一个`x`出现

## re 模块

### re 方法

- list findall(re,string)
- boolean search(re,string)
- boolean match(re,string)

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

- `?P<id>` 是给 分组\d+起的名字为id
- `<em .*?>(?P<id>\d+).*?<span class="title">`
- '8-2*5/3 + 7 /3*99/4*2998 +10 * 568/14' 从一个没有括号的表达式中取 */法 == 正则表达式

## 转义问题

`re.findall(r'\\s', r'\s')`

