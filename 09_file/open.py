# 文件路径
filePath = './cn.txt'
# filePath = './README.md'
# filePath = '';


# f = open(filePath, mode='r', encoding='utf-8')
f = open(filePath, mode='r', encoding='GBK')

# 读
content = f.read()

# 输出
print(content)

# 关闭
f.close()