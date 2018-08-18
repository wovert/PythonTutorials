lis = [2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']
'''
# 1)将列表lis中的’tt’变成大写（用两种方式）。
# lis[3][2][1][0] = "TT"
# print(lis)
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis2)
# 2)将列表中的数字3变成字符串’100’（用两种方式）。
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# print(lis)
# lis[3][2][1].remove(3)
# lis[3][2][1].insert(1,'100')
# print(lis)
'''
# 3)将列表中的字符串’1’变成数字101（用两种方式）
# lis[3][2][1][2] = 101
# print(lis)
# lis[3][2][1][2] = int(lis[3][2][1][2].replace('1','101'))
# print(lis)
# print(lis[3][2][1][2])  # '1'
# lis[3][2][1][2] = int('10'+lis[3][2][1][2])
# lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
# li = [1,2,3]
# li[2] = 33
# print(li)
# 5,查找列表li中的元素，移除每个元素的空格，
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
# li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]
li = ['taibai ','alexC','AbC ','egon',' Ritian',' Wusir','  aqc']
b=[]
# for i in li:
#     s=i.strip()
#     if (s.startswith("A")or s.startswith("a"))and s.endswith("c"):
#         b.append(s)
# for x in b:
#     print(x)
 
# for i in li:
#     s=i.strip()
#     if s[0].upper() == 'A' and s[-1] == 'c':
#         b.append(s)
# for x in b:
#     print(x)
# 6、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
 
# li=["苍老师","东京热","武藤兰","波多野结衣"]
# new_li= []
# info = input("评论")  # 苍老师，东京热 法律框架第三
# for i in li:
#     if i in info:
#         l = len(i)
#         info=info.replace(i,'*'*l)
# new_li.append(info)
# print(new_li)