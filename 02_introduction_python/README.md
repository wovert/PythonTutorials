# Introduction Python

## Why is Python

- 谷歌
  - Google App Engine
  - code.google.com
  - Google earth
  - 谷歌爬虫
  - Google广告等项目都在大量使用 Python 开发
- CIA：美国中央情报局网站用 Python 开发的
- NASA: 美国航天局大量使用 Python 进行数据分析和运算
- YouTube：世界上最大的视频网站用 Python 开发的
- Dropbox: 美国最大的在线云存储网站，全部用 Python 实现
- Instagram：美国最大的图片分享社交网站
- Facebook: 大量的基础库均通过 Python 实现的
- RedHat： yum 包管理工具就是用 Python 开发
- 豆瓣：公司几乎所有的业务均是通过 Python 开发的
- 知乎：国内最大的问答社区，通过 Python 开发（国外Quora）
- 春雨医生：国内知名的在线医疗网站是用 Python 开发的
- 搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝、土豆、新浪、果壳等公司都在使用 Python 完成各种各样的任务

## What is Python

> 1989年，圣诞节期间，Guido 开始写 Python 语言的编译器。Python 名字来自 Guido 所挚爱的电视剧 Monty Python's Flying Circus。
> 1991年，第一个 Python 编译器诞生。用C语言实现的，并能够调用C语言的库文件
> 介于 C 和 shell 之间，功能全面、易学易用、可扩展的语言
> 实现了类、函数、异常处理、表和词典在内的核心数据类型，以及模块为基础的扩展系统

## Python Features

- 编程语言
- 语法简洁、优雅、编写的程序容易阅读
- 跨平台（可运行在Windows、Linux和MacOS）
- 易于学习（相比于其他编程语言）
- 丰富标准库与第三方库（电子邮件、图形GUI界面）
- 支持面向对象

## Python Philosoph

- Simple is better thant complex. 简洁生于复杂
- Now is better that never. Although newver is often better than right now. 做也许好过不做，但不假思索就动手还不如不做

## Python Hitory

- Python 1.0 - January 1994 增加了lambda, map, filter and reduce
- Python 2.0 - October 16, 2004，加入了内存回收机制
- Python 2.4 - November 30, 2004，最流行的Web框架Django诞生
- Python 2.5 - September 19, 2006
- Python 2.6 - October 1, 2008 (过渡版本，兼容2.4和3.0)
- Python 2.7 - July 3, 2010 主流工业版本

- In November 2014, it was announced that Python 2.7 would be supported until 2020, and reaffirmed that there would be no 2.8 release as users were exprected to move to Python 3.4+ as soon as possible
- Python 3.0 - December 3, 2008
- Python 3.1 - Jun 27, 2009
- Python 3.2 - February 20, 2011
- Python 3.3 - September 29, 2012
- Python 3.4 - March 16, 2014
- Python 3.6 - September 13, 2015

### Python2 VS PYthon3

- Python2 不标准，代码混乱
- Python3 标准化

### Python 的环境

- 编译型：一次性将所有程序编译成二进制文件
  - 缺点：开发效率低、不能跨平台
  - 优点：运行速度快
  - 语言：C/C++, Object-C, swift, Go,, Pascal
  - 应用：系统级开发(游戏)
- 解释型：程序执行时，逐行的解释
  - 优点：开发效率高，跨平台
  - 缺点：运行速度慢（相对于编译型语言）
  - 语言：Python, PHP, Perl, Ruby, JavaScript, Erlang
  - 应用：应用程序开发

- 混合型:
  - 语言：Java, C#

## Python Application

- Web Programming: Django/Pyramid/Bottle/Tornado/Flask/Web2py
- Network Programming: Twisted/Requests/Scrapy/Paramiko/BeautifulSoup
- GUI Development: wxPython/tkInter/PyGtk/PyGObject/PyQt
- Scientific and Numeric: SciPy/Pandas/IPython
- Software Development: Buildbot/Trac/Roundup
- System Administration: Ansible/SaltStack/OpenStack/腾讯蓝鲸

## Python 应用领域

- 自动化运维
- 自动化测试
- 大数据分析
- 科学计算
- GUI开发
- 系统编程
- 爬虫
- AI
- Web开发

## Python 程序

[Python socket局域网聊天与文件传输](http://www.codesky.net/showhtml/22087.htm)

[12306火车票抢票软件源码](http://www.codesky.net/showhtml/25003.htm)

[python实现ping命令](http://www.codesky.net/showhtml/22088.htm)

[Python采集百度地图数据](http://www.codesky.net/showhtml/22392.htm)

[mysql封装类](http://www.codesky.net/showhtml/22391.htm)

## Python 程序执行过程

- source code(.py) -> Compile -> bytecode(.pyc)->Interpreter(PVM) -> processor