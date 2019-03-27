# str --->byte  encode 编码
s = '二哥'
b = s.encode('utf-8')
print(b)

# byte --->str decode 解码
s1 = b.decode('utf-8')
print(s1)
 
 
s = 'abf'
b = s.encode('utf-8')
print(b)

# byte --->str decode 解码
s1 = b.decode('gbk')
print(s1)