# 正则表达式
# 字符组 [字符]
# 元字符
    # \w \d \s
    # \W \D \S
    # . 除了换行符以外的任意字符
    # \n \t
    # \b
    # ^ $ 匹配字符串的开始和结束
    # （） 分组  是对多个字符组整体量词约束的时候用的
                #re模块：分组是有优先的
                    # findall
                    # split
    # | 从左到右匹配，只要匹配上就不继续匹配了。所以应该把长的放前面
    # [^] 除了字符组内的其他都匹配
# 量词
    # *   0~
    # +   1~
    # ？  0~1
    # {n} n
    # {n,} n~
    # {n,m} n~m
 
# 转义的问题
# import re
# re.findall(r'\\s',r'\s')
 
# 惰性匹配
# 量词后面加问号
    # .*?abc 一直取遇到abc就停
 
# re模块
# import re
# re.findall('\d','awir17948jsdc',re.S)
# 返回值：列表 列表中是所有匹配到的项
 
# ret = search('\d(\w)+','awir17948jsdc'）
# ret = search('\d(?P<name>\w)+','awir17948jsdc'）
# 找整个字符串，遇到匹配上的就返回，遇不到就None
# 如果有返回值ret.group()就可以取到值
# 取分组中的内容 ： ret.group(1)   /  ret.group('name')
 
# match
# 从头开始匹配，匹配上了就返回，匹配不上就是None
# 如果匹配上了 .group取值
 
# 分割 split
# 替换 sub 和 subn
# finditer 返回迭代器
# compile 编译 ：正则表达式很长且要多次使用
 
import re
 
# ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
# #还可以在分组中利用?<name>的形式给分组起名字
# #获取的匹配结果可以直接用group('名字')拿到对应的值
# print(ret.group('tag_name'))   #结果 ：h1
# print(ret.group())             #结果 ：<h1>hello</h1>
 
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# #如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
# print(ret.group(1))
# print(ret.group())  #结果 ：<h1>hello</h1>
 
import re
 
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']
# ret.remove('')
# print(ret)
# ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '-2', '60', '', '5', '-4', '3']
# ret.remove("")
# print(ret) #['1', '-2', '60', '5', '-4', '3']
 
# 首先得到一个字符串
# 去空格
# 没有空格的字符串
# 先算最里层括号里的 ： 找括号 ，且括号里没有其他括号
# 得到了一个没有括号的表达式 ：只有加减乘除 从左到右先找到第一个乘除法   —— 重复
# 所有的乘除法都做完了
# 计算加减  —— 加减法
# 只有一个数了 就可以结束了