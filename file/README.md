# 文件
## 文件扩展名
- web文件：.html, .css, .js, .xml, .json
- 程序：.php, .py, .rb, .c, .cc
- 视频：.flv, avi, .rmvb, .mp4, .mkv, .3gp
- 音频：.wmv, .mp3, .flue, .mid, 
- 其他：.pdf, .chm

- `f = open(/path/to/SOMEFILE, mode, encode='utf8')`
- `data = f.read(5) 5个字符`
- `f.close()`
- 读取一行
`f.readline()` 

- 读取所有行以列表显示
`for i in f.readlines():
	print(i.strip())`

- 列表连接成字符串
`''.join([.strip(), 'iiii'])`

- 文件对象转换成迭代器
`for i in enumerate(f.readlines()):`

- 返回指针位置
`f.tell()`

- 移动指针到起始首行
`f.seek(0)`

- with语句不用关闭close()方法
`with open(/path/to/somefile, r) as f,open(/path/to/somefile, w) as f2 :
	f.read()
	f2.write()`