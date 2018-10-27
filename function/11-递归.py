#4! = 4*3*2*1
#5! = 5*4*3*2*1
'''
i = 1
result = 1
while i<=4:
    result = result * i
    i+=1

print(result)
'''


#5! => 5*4!
#4! => 4*3!

'''
def xxx(num):
    num * xxxx(num-1)

def xx(num):
    num * xxx(num-1)

def getNums(num):
    num * xx(num-1)

getNums(4)
'''



def getNums(num):
    if num>1:
        return num * getNums(num-1)
    else:
        return num

result = getNums(4)
print(result)












