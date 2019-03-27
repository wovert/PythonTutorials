# 变量

## 变量命名规则

- 字母、数字和下划线组成且不能以数字开头
- 区分大小写
- 不能使用python关键字和保留字
  - 关键字：`and,as,assort,break, class, continue,def, del,elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield`

## 变量名命名约定

- 定义变量名有意义
- 驼峰式命名和下划线分割单词
- 全部大写的变量名来代表常量

## 变量特性`ls -al`

- python 不区分变量和常量，都是变量
- Python 的变量都是可变的

## 定义变量

- 单引号定义: `msg='hello'`
- 双引号定义: `msg="hello"`
- 三个单引号定义

```py
msg='''
hello
world'''
```

- 三个双引号定义

```py
msg="""
hello
world"""
```

## 销毁变量

- `del 变量名`
- `age = nil`

## 注释

> 注释用于增强程序源代码可读性

`# 单行注释`

``` Python
'''
多行注释
'''`

"""
多行注释
"""
```