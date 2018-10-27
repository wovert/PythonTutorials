def test(a,b,func):
    result = func(a,b)
    return result


num = test(11,22,lambda x,y:x+y)
print(num)
