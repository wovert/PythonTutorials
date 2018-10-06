#a = 100
a = [100]

def test(num):
    #num+=num#  +=表示 num指向谁就对谁进行修改,如果num指向[100],那么就变为[100,100]
                #如果num 指向100,因为100是不可变类型,所以不能修改,所以num=num+num

    num = num+num#===>[100] + [100] ====>[100,100]   注意只要是num=xxx一定是num指向了一个新的地方
    print(num)

test(a)

print(a)
