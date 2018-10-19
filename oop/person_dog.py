# 人狗大战
def Dog(name,blood,aggr,kind):
    dog = {
        'name': name,
        'blood': blood,  # 血量
        'aggr': aggr,  # 攻击力
        'kind': kind,
    }
    def bite(person):
        person['blood'] -= dog['aggr']
        print('%s被咬了，掉了%s的血' % (person['name'], dog['aggr']))
    dog['bite'] = bite
    return dog
 
def Person(name,blood,aggr,sex):
    person = {
        'name' : name,
        'blood': blood,   # 血量
        'aggr': aggr,      # 攻击力
        'sex':sex,
    }
    def attack(dog):
        dog['blood'] -= person['aggr']
        print('%s被打了，掉了%s的血' % (dog['name'], person['aggr']))
    person['attack'] = attack
    return person
 
# 代码精简了 方便增加人物 方便修改 人物更加规范  —— 人模子
 
 
 
jin = Dog('金老板',1000,100,'teddy')
alex = Person('狗剩儿',100,1,'不详')
# nezha = Person('哪吒',200,2,'不详')
print(jin)
jin['bite'](alex)
alex['attack'](jin)
# Dog函数和Person函数 都是定义了一类事物
# 直到调用了函数，赋值了之后才真的有了一个实实在在的人或狗
 
 
# 面向对象编程
# 所谓模子 就是 类 抽象的 我能知道有什么属性 有什么技能 但不能知道属性具体的值
# jin alex nezha 就是对象 有具体的值，属性和技能都是根据类规范的