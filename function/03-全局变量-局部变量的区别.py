'''
def get_wendu():
    wendu = 33
    return wendu

def print_wendu(wendu):
    print("温度是%d"%wendu)

result = get_wendu()#如果一个函数有返回值,但是没有在调用函数之前 用个变量保存的话,那么没有任何的意义
print_wendu(result)
'''

#定义一个全局变量,wendu
wendu = 0

def get_wendu():
    #如果wendu这个变量已经在全局变量的位置定义了,此时还想在函数中对这个全局变量进行修改的话
    #那么 仅仅是 wendu=一个值  这还不够,,,此时wendu这个变量是一个局部变量,仅仅是和全局变量的名字
    #相同罢了
    #wendu = 33
    
    #使用global用来对一个全局变量的声明,那么这个函数中的wendu=33就不是定义一个局部变量,而是
    #对全局变量进行修改
    global wendu
    wendu = 33

def print_wendu():
    print("温度是%d"%wendu)

get_wendu()
print_wendu()
