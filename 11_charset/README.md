# 编码

- Python2 默认ASCII占用2个字节
- Python2 默认UTF-8占用3个字节

Unicode 占用4个字节, 一个中文占用4个字节

UTF-8 一个中文 3个字节表示,英文字母8位一个字节，欧洲16位，2个字节，中文24位，3个字节

GBK 中文字符集，一个中文占用两个字节(65535 汉字)，英文1个字节

python2文件中声明utf-8字符方法

```py
#coding=utf-8

Python官网推荐使用
#-*- coding:utf-8 -*-
```
