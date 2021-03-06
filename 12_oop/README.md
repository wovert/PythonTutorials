# Object Oriented Programming

- 程序 = 指令 +　数据
- 代码可以选择以指令为核心或以数据为核心进行编写
- 以指令为核心：围绕“正在发生什么”进行编写
- 面向过程编程：程序具有一系列线性步骤；主体思想是代码作用于数据
- 以数据为核心：围绕“将影响谁”进行编写
- 面向对象编程：围绕数据及为数据严格定义的接口来组织程序，用数据控制对代码的访问。
- 面向过程；程序＝算法+数据结构
- 面向对象：将问题空间中的元素以及它们在解空间中的表示物抽象为对象，并允许实例想象成一种新型变量，它保存着数据，大你可以对自身的数据执行操作。

- 面向过程：一件事该怎么做
  - 狗.吃(东西)
- 面向对象：一件事该让谁来做，那个谁就是对象
  - 吃.(狗,东西)

1. 构造对象的方法 __new__
2. 初始化对象的方法(已经得到了对象 self`) __init__

`__str__ === toString()`

## 类的关系

- 依赖(uses-a) 一个类的方法操作另一个类的对象
- 聚合(has-a) 类 A 的对象包含类 B 的对象
- 继承(is-a) 描述特殊与一般关系

- 类中的静态变量 可以被对象和类调用
- 对于不可变数据类型来说，类变量最好用类名操作
- 对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的

- 类里的名字有 类变量（静态属性量）+ 方法名（动态属性）
- 对象里的名字 对象属性
- 对象 ——> 类
- 对象找名字 ： 先找自己的 找类的 再找不到就报错
- 对象修改静态属性的值
  - 对于不可变数据类型来说，类变量最好用类名操作
  - 对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的

### 组合

一个对象的属性值是另外一个类的对象

### 继承

- `C.__mro__` 查看C类继承关系
- 一个类 可以被多个类继承
- 一个类 可以继承多个父类  —— python里

- 父类中没有的属性 在子类中出现 叫做派生属性
- 父类中没有的方法 在子类中出现 叫做派生方法
- 只要是子类的对象调用，子类中有的名字 一定用子类的，子类中没有才找父类的，如果父类也没有报错
- 如果父类 子类都有 用子类的
  - 如果还想用父类的，单独调用父类的:
  - 父类名.方法名 需要自己传`self`参数
  - `super().方法名` 不需要自己传`self`
- 正常的代码中 单继承 === 减少了代码的重复
- 继承表达的是一种 子类是父类的关系

- 单继承
  - 先抽象再继承，几个类之间的相同代码抽象出来，成为父类
  - 子类自己没有的名字，就可以使用父类的方法和属性
  - 如果子类自己有，一定是先用自己的
  - 在类中使用`self`的时候，一定要看清楚self指向谁
- 多继承
  - 新式类和经典类：
    - 多继承寻找名字的顺序 ： 新式类广度优先，经典类深度优先
    - 新式类中 有一个类名`.mro`方法，查看广度优先的继承顺序
    - python3中 有一个`super`方法，根据广度优先的继承顺序查找上一个类
    - __init__() 初始化方法中， `super().__init()__` 主动调用

### 接口

- `raise NotImplemented` 抛出异常