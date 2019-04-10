0# 文件

## 文件扩展名

- web文件：.html, .css, .js, .xml, .json
- 程序：.php, .py, .rb, .c, .cc
- 视频：.flv, avi, .rmvb, .mp4, .mkv, .3gp
- 音频：.wmv, .mp3, .flue, .mid
- 其他：.pdf, .chm

## 文件操作

> 以存储文件编码方式方式打开文件

- 举例：以GBK保存的文件，以GBK编码方式打开
- Pycharm 默认 utf-8文件创建并存储
- 文件编码和文件内容编码必须要统一，否则打开文件会显示乱码内容

``` PYTHON

# utf-8编码方式打开，Python3 字符串以unicode编码，unicode 隐式转换为 utf-8
# open函数内部 byte 类型转化为 str类型
f = open(filePath, mode='r', encoding='utf-8')
f = open(filePath, mode='r', encoding='GBK')
```

### mode

- r: 读取
- rb: 二进制读取

- str 转 bytes : `"中文".encode('utf-8')`

``` py
f = open('/path/to/SOMEFILE', mode, encode='utf8')
data = f.read(5)  # 5个字符
f.close()
```

- 读取一行：`f.readline()`

- 读取所有行以列表显示

``` py
for i in f.readlines():
  print(i.strip())
```

- 列表连接成字符串

``` PYTHON
''.join([.strip(), 'iiii'])
```

- 文件对象转换成迭代器: `for i in enumerate(f.readlines()):`

- 返回指针位置: `f.tell()`

- 移动指针到起始首行: `f.seek(0)`

- with语句不用关闭close()方法

``` PYTHON
with open(/path/to/somefile, r) as f,open(/path/to/somefile, w) as f2 :
  f.read()
  f2.write()
```