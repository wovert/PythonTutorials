# Setup Python

## Python 语言环境集成开发环境

[Python 官方下载](http://python.org)

[Pycharm 下载](http://jetbrains.com)

## pycharm 配置

Settings->Editor->File and Code Templats -> Python Script

``` Python
#__author__ = '${USER}'
#date = ${DATE}
```

## 执行 Python 方法

### 方法1

`$ python python_file.py`

### 方法2

``` shell
文件首行带有解释器声明
#!/usr/bin/env python 或 #!/usr/bin/python3

授予文件有执行权限：
$ chomw u+ python_file.py

执行文件
$ ./python_file.py
```

## Python 2 or Python 3

> milestone Python-3.x: http://twistedmatrix.com/trac/milestone/Python-3.x

- Python2           Python3
- print             print()
- `_winreg`           winreg
- ConfigParser      configparser
- copy_reg          copyreg
- Queue             queue
- markupbase        `_markupbase`
- repr              reprlib
- test.test_support test.support
- 1/2=0             1/2=0.5
- raw_input         input
- class Foo:        class Foo(object)

## 字符编码

- 2.x 默认编码 **ASCII** 码（不支持中文)
  - 支持中文方式，文件编码
    - `#-*- coding:utf-8 -*-` 官网推荐方式
    - `#coding=utf-8`
  - `u"中文编码"`
    - type(us) # unicode 类型
    - unicode 编码 向下兼容 gb2312 和 gbk

- 3.x 默认编码是 **UNICODE** (支持中文)

- 1980年(6700+)    gb2312
- 1995年(20k)      GBK
- 2000年(27k)      gb18030（包括繁体字）
- big5 台湾

- unicode 65535，支持所有国家和地区的编码
  - 存一个字符，同一占用2个字节
- utf-8 65535
- unicode 的扩展集，解决占用空间问题，可变长的字符编码
  - ASCII 占用1个字节
  - 欧洲的字符占用2个字节
  - 东亚的字符3个字节，汉字占用**3个字节**

- Python2 字符编码默认是 ASCII
- Python2 GBK 转换 UTF-8
  - GBK 转换 Unicode 编码
  - Unicode 转换 UTF-8 编码

- Python2 GBK 转换 UTF-8 格式流程：默认是 ASCII

1. 编码[decode]转换为 Unicdoe 编码
2. 解码[encode]转换为 utf-8 编码

> 默认是 utf-8

`sys.getdefaultencoding()`

## Python 种类

- CPython: 原始、标准的实现方式, C解释器 .pyc(字节码) 机器码 CPU
- Jython: 用于与Java语言集成的实现,java解释器 java字节码 机器码 CPU
- IronPython: 用于与.Net框架集成的实现, C#解释器 C#字节码 =》 机器码 CPU
- pypy: 解释器 字节码 机器码 => CPU

## Python 多版本环境搭建 - CentOS OS 安装开发环境

### Python 多版本共存配置

- 关于环境变量：可执行文件包含到PATH环境变量中
- 安装python多个版本之后，在python.exe和pip.exe所在目录下复制一份python-版本名.exe和pip-版本名.exe文件。按照优先顺序版命令所在目录追加到path 环境变量当中。

``` shell
# echo $PATH
# whereis python
# ln -s /usr/bin/python3.5 /usr/bin/python3
# ln -s /usr/bin/python2.7 /usr/bin/python2
# python3
# python2

配置默认python
# rm /usr/bin/python
# ln -s /usr/bin/python3.5 /usr/bin/python
```

- Pycharm配置
  - 新建项目(Pure Python -> Interpreter: 选择版本)
  - 新建hello.py 文件之后执行文件
  - 在 run 窗口显示运行python 版本

  - 更换 Python 版本
  - Settings -> Project: 名字 -> Project Interpreter -> 选择版本 -> OK
  - 任务栏中切换版本切换
  - 运行程序，在run 窗口中显示相应切换版本

``` shell
# yum -y groupinstall "Development Tools"
# yum -y install readline readline-devel readline-static openssl openssl-devel openssl-static zlib-devel bzip2-devel ncurses-devel sqlite-devel  tk-devel gdbm-devel db4-devel libpcap-devel xz-devel bzip2-devel bzip2-libs git build-essential zlib1g-dev libssl-dev libsqlite3-dev libbz2-dev libreadline-dev libreadline-dev
```

### pyenv 安装

``` shell
# git clone https://github.com/yyuu/pyenv.git ~/.pyenv

将 PYENV_ROOT 和 pyenv init 加入 bash的 ~/.bashrc
# echo 'export PATH=~/.pyenv/bin:$PATH' >> ~/.bashrc
# echo 'export PYENV_ROOT=~/.pyenv' >> ~/.bashrc
# echo 'eval "$(pyenv init -)"' >> ~/.bashrc
# source ~/.bashrc

查看可安装的版本
# pyenv intsall --list`
```

- anaconda-2.0.1  支持Python 2.6和2.7
- anaconda3-2.0.1 支持Python 3.3和3.4

其中形如x.x.x这样的只有版本号的为Python官方版本，其他的形如xxxxx-x.x.x这种既有名称又有版本后的属于“衍生版”或发行版

安装指定版本: `# pyenv install 3.5.4`

该命令会从github上下载python的源代码，并解压到/tmp目录下，然后在/tmp中执行编译工作。若依赖包没有安装，则会出现编译错误，需要在安装依赖包后重新执行该命令对于科研环境，更推荐安装专为科学计算准备的Anaconda发行版，pyenv install anaconda-2.1.0安装2.x版本，pyenv install anaconda3-2.1.0安装3.x版本
Anacoda很大，用pyenv下载会比较慢，可以自己到Anaconda官方网站下载，并将下载得到的文件放在~/.pyenv/cache目录下，则pyenv不会重复下载

- 卸载指定的 Python：`# pvenv uninstall 3.5.4`

- 更新数据库：`# pyenv rehash`

- 查看当前已安装的 Python 版本

`# pyenv versions`

`* system`表示当前正在使用的是系统自带的 Python

- 设置全局 Python 版本

``` shell
# pyenv global 3.5.4
# pyenv version
```

- 临时改变 Python 版本

``` shell
# pyenv local
# pyenv shell
```

- 切换的 Python 版本

`# pyenv global system`

- 切换到 Python 版本

`# pyenv shell或者local 3.5.4`

- 示例代码

``` shell
# mkdir python354 && cd python354
# pyenv local 3.5.4```
```

当前工作目录使用 Python 3.5.4 版本

`# python -V` 查看版本

`# pip -V`查看一下 pip 版本

输入python即可使用新版本的python
系统自带的脚本会以/usr/bin/python的方式直接调用老版本的python，因而不会对系统脚本产生影响

使用pip安装第三方模块时会安装到~/.pyenv/versions/3.4.1下，不会和系统模块发生冲突

使用pip安装模块后，可能需要执行pyenv rehash更新数据库

### virtualenv 安装

- 开发环境应用独立
- 环境升级不影响其他应用，也不会影响全局的Python 环境
- 防止系统中出现包管理混乱和版本的冲突

``` shell
setup
# pip install virtualenv

create env
# virtualenv virtualName
# cd virtualName/Scripts
# activate.bat 进入虚拟环境
# pip list
# deactive.bat 退出虚拟环境
```

### virtualenvwrapper-win(Windows OS 加 win)

``` shell
# pip install virtualenvwrapper

创建虚拟环境 -> 自动进入虚拟环境
# mkvirtualenv virenv

删除虚拟环境 - 自动进入虚拟环境:
# rmvirtualenv virenv

推出虚拟环境
scripts> deactivate

查看有哪些虚拟环境
scripts> workon

进入虚拟环境
scripts> workon virenv

显示开发包
(virenv) > pip list

安装开发包
# pip install requests

卸载开发包
# pip uninstall requests
```

### pyenv-virtual

> pyenv-virtual 是 pyenv 的插件，支持管理多个 virtualenv

``` shell
Setup
# git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

Create virtualenv
# pyenv virtualenv 版本号 虚拟环境名称

Delete virtualenv
# pyenv uninstall 虚拟环境名称

列表 virtualenv
# pyenv virtualenvs

激活/禁用 virtualenv
# pyenv active <virtualev-name>
# pyenv deactivate

Create Virtual Env
# pyenv virtualenv 3.5.4 venv-3.5.4
# mkdir myproject && cd myproject
# pyenv local venv-3.5.4

pyenv-virtualenv
# deactivate

pyenv-virtualenv
# activate venv-3.5.1

只要我们进入myproject目录，就会自动激活virtualenv，退出myproject目录，就会关闭virtualenv

如果要关闭自动激活，可以运行命令pyenv deactivate，要重新启用的话，运行pyenv activate 虚拟环境名
```

### 安装 ipython

``` shell
# yum -y install ipython
# yum -y install ipython3
```

### Python 性能优化工具

#### Psyco

> Python语言的一个扩展模块，可以即时对程序代码进行专业的算法优化，可以在一定程度上提高程序的执行效率，尤其是在进程中大量循环操作时

目前开发已经停止，有PyPy所接替

#### PyPy

> 用Python实现的Python解释器

Python语言的动态编译器，是Psyco的后继项目可以运行在Linux的32bit和64 bit，MacOSX和Windows32bit平台中

#### Shed Skin

> Python编译器，python代码转换成优化的C++代码
> 性能要求高的使用GO语言（Docker）

## Computer Language History

- 1973, C
- 1983, C++
- 1987, perl(Larry Wall)
- 1989, Linux，Python  
- 1991, Python 正式版本，苏联解体，东西德合并
- 1994, PHP, Netscape
- 1995, Java, ruby(Ruby on rails)
- 2009, Go

- scalar：大数据开发
- erlang: 面向并发编程
- javascript: 前段语言
  - nodejs
- vb: 微软, bat脚本
  - C#
- lua: nginx脚本语言

## Python 调试

- pdb 调试：python -m pdb name.py 
  - l :list 显示当前的代码
  - n :next 向下执行一行代码
  - c :continue 继续执行代码
    - c breakNum: 执行到断点号
  - b linenumber: break 添加断点
    - c
  - clear breakNum: 删除断点
  - s : step 进入到一个函数
    - a : 打印所有形参
    - r : return 快速执行到函数的最后一行
  - p 变量： print 打印一个变量

交互调试

``` py
def test(a,b):
  c = a + b
  return c

import pdb
pdb.run("test(11,22)")
```

程序里埋点

``` Python
impor pdb
pdb.set_trace()
```

``` shell
# python3 name.py
```

自动停在 `pdb.run("test(11,22)")` 之上

日志调试

``` Python
import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
```

然后热修复

## Anaconda

> [anaconda 官网](https://www.anaconda.com)

``` shell
setup
# conda install 库名

update
# conda update 库名
```

## 爬虫常用库的安装

### Windows 安装过程

#### 检查 urllib 和 re 内置库

``` py
>>> import urllib
>>> import urllib.request
>>> urllib.request.urlopen('http://www.baidu.com')

>>> import re
```

#### 安装 requests 库

``` py
> pip3.6 install requests
> python3
> import requests
> requests.get('http://www.wovert.com')
```

#### 安装 selenium 库(自动化测试库-驱动浏览器)

``` py
> pip3.6 install selenium
> python3
> from selenium import webdriver
提示找不到chromedriver程序
```

#### 下载安装 chromedriver 程序

`chromedriver.exe` 文件放到 `python36/Scripts`目录下

``` py
>>> from selenium import webdriver
>>> driver = webdriver.Chrome()
闪退原因：chromedriver与chrome版本不兼容，下载兼容chrome浏览器的chromedriver版本

>>> driver.get('https://www.python.org')

打印网页源代码
>>> driver.page_source

```

#### 无界面浏览器 [phantomjs.org](http://phantomjs.org)

1. 解压文件找到 phantomjs.exe
2. phantomjs.exe所在目录，配置到PATH环境变量

``` shell
# phantomjs
phantomjs > conosle.log('hello world')
```

``` py
>>> from selenium import webdriver
>>> driver = webdriver.PhantomJS()
>>> driver.get('https://www.python.org')
>>> driver.page_source
```

#### 安装 lxml 库(xpath解析库)

``` py
>>> pip3.6 install lxml
下载很慢
```

- 解决方案:
  - [lxml](https://pypi.python.org/pypi/lxml/3.7.3)
- 下载文件是`lxml-xxxx.whl`，但前提是必须先安装 `pip3 install wheel`

``` py
>>> pip3.6 install wheel
>>> pip3.6 uninstall lxml
>>> pip3.6 install C:\donwload\lxml-xxx.whl
```

#### 安装 beautifulsoup

> 依赖于 lxml库

``` py
>>> pip3.6 install beautifulsoup4
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup('<html></html>','lxml')
```

#### 安装 pyquery

``` py
>>> pip3.6 install pyquery
>>> from pyquery import PyQuery as pq
>>> doc = pq('<html>hello</html>')
>>> result = doc('html').text()
>>> result
hello
```

#### 安装 pymysql(用于python3.6)

``` py
>>> pip3.6 install pymysql
>>> python
>>> import pymysql
>>> con = pymysql.connect(host='localhost',user='root',password='123456',port=3306, db='mysql')
>>> cursor = con.cursor()
>>> cursor.execute('select * from db')
>>> cursor.fetchone()
```

#### 安装 pymongo

``` py
>>> pip3.6 install pymongo
>>> python
>>> import pymongo
>>> client = pymongo.MongoClient('localhost')
>>> db = client['newtestdb']
>>> db['table'].insert({'name':'Alice'})
>>> db['table'].find_one({'name':'Alice'})
```

#### 安装 redis

> 用于分布式爬虫队列

``` py
>>> pip3.6 install redis
>>> python
>>> import redis
>>> r = redis.REdis('localhost',6377)
>>> r.set('name', 'Alice')
>>> r.get('name')
b'Alice'
```

#### 安装 flask

> Web框架库

``` py
>>> pip3.6 install flask
>>> python
>>> import flask
```

#### 安装 django

> Web服务器框架

``` py
>>> pip3.6 install django
>>> python
>>> import django
```

#### 安装 jupyter

> 记事本库，编写markdown文档，依赖于ipython库

``` cmd
> jupyter notebook
打开浏览器创建文件并输入测试代码并运行，会输出运行结果

### title

Ctrl + Enter 保存
```

### Linux/Mac 安装

``` sh
# pip3 install requests selenium beautifulsoup4 pyquery pymysql pymongo redis flask django jupyter
```